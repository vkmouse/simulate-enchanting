from core import EnchantmentAttribute, EnchantmentRange

def _removeSymbol(str: str):
    res = ''
    for ch in str:
        if not(ch == '+' or ch == '-' or ch == '%' or ch == '~' or ch==' ' or ch==',' or ch.isdigit()):
            res += ch
    return res

def _findPercentage(itemName: str):
    return '%' in set(itemName)

# expr: EOS | (EMPTY | MINUS) term
# term: factor TILDE factor | factor (COMMA factor)*
# factor: INTEGER

class RangeLexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0

    def getNextToken(self) -> dict[str, str]:
        output = { 'Type': 'EOS', 'Value': '' }
        while not self.eos:
            if self.current.isdigit():
                output = { 'Type': 'INTEGER', 'Value': self.integer() }
                break
            elif self.current == '~':
                self.advance()
                output = { 'Type': 'TILDE', 'Value': '~' }
                break
            elif self.current == ',':
                self.advance()
                output = { 'Type': 'COMMA', 'Value': ',' }
                break
            elif self.current == '-':
                self.advance()
                output = { 'Type': 'MINUS', 'Value': '-' }
                break
            elif self.current == '減' and self.peek() == '少':
                self.advance()
                self.advance()
                output = { 'Type': 'MINUS', 'Value': '-' }
                break
            else:
                self.advance()
        return output

    def integer(self) -> str:
        num = ''
        while self.current.isdigit() and not self.eos:
            num += self.current
            self.advance()
        return num

    def advance(self):
        self.pos += 1

    def peek(self):
        if self.pos + 1 > len(self.text) - 1:
            return ''
        else:
            return self.text[self.pos + 1]

    @property
    def current(self) -> str:
        if self.pos > len(self.text) - 1:
            return ''
        else:
            return self.text[self.pos]

    @property
    def eos(self) -> bool:
        return self.current == ''

class RangeCalculator:
    def __init__(self):
        self.numbers = []
        self.isNegative = False
        self.isDiscrete = False

    def append(self, number: int):
        self.numbers.append(number)
    
    def calculate(self) -> EnchantmentRange:
        output: EnchantmentRange = { 'Start': 0, 'Stop': 0, 'Step': 1 }
        if len(self.numbers) > 0:
            output['Start'] = self.numbers[0]
            output['Stop'] = self.numbers[-1]
        if self.isDiscrete:
            output['Step'] = self.numbers[1] - self.numbers[0]
            for i in range(len(self.numbers) - 1):
                if self.numbers[i] + output['Step'] != self.numbers[i + 1]:
                    raise Exception('numbersToRange failed')
        if self.isNegative:
            output['Start'], output['Stop'] = -output['Stop'], -output['Start']
        return output
        
class RangeParser:
    def __init__(self, text: str):
        self.lexer = RangeLexer(text)
        self.currentToken = self.lexer.getNextToken()
        self.rangeNode = RangeCalculator()
    
    def parse(self) -> EnchantmentRange:
        self.expr()
        return self.rangeNode.calculate()

    def expr(self):
        if self.currentType == 'EOS':
            self.eat('EOS')
        else:
            if self.currentType == 'MINUS':
                self.eat('MINUS')
                self.rangeNode.isNegative = True
            self.term()

    def term(self):
        self.factor()
        if self.currentType == 'TILDE':
            self.eat('TILDE')
            self.factor()
        else:
            while self.currentType == 'COMMA':
                self.rangeNode.isDiscrete = True
                self.eat('COMMA')
                self.factor()

    def factor(self):
        self.rangeNode.append(int(self.currentToken['Value']))
        self.eat('INTEGER')

    def eat(self, Type):
        if self.currentType == Type:
            self.currentToken = self.lexer.getNextToken()
        else:
            raise Exception('Invalid syntax')

    @property
    def currentType(self):
        return self.currentToken['Type']

class Parser:
    def parseRange(self, itemName: str):
        return RangeParser(itemName).parse()

class CriticalDamageParser(Parser):
    def match(self, itemName: str):
        return itemName.find('必殺技傷害增加') != -1 or itemName.find('暴擊傷害') != -1
    
    def parse(self, itemName: str) -> EnchantmentAttribute:
        return {
            'Category': {
                'Name': '暴擊傷害',
                'IsPercentage': True
            },
            'Range': self.parseRange(itemName)
        }

class DelayAfterAttackParser(Parser):
    def match(self, itemName: str):
        return itemName.find('攻擊後延遲') != -1
    
    def parse(self, itemName: str) -> EnchantmentAttribute:
        return {
            'Category': {
                'Name': '攻擊速度增加(攻擊後延遲)',
                'IsPercentage': True
            },
            'Range': self.parseRange(itemName)
        }

class DelayAfterSkillParser(Parser):
    def match(self, itemName: str):
        return itemName.find('技能') != -1 and itemName.find('後延遲') != -1

    def parse(self, itemName: str) -> EnchantmentAttribute:
        return {
            'Category': {
                'Name': '技能後延遲',
                'IsPercentage': True
            },
            'Range': self.parseRange(itemName)
        }

class GeneralParser(Parser):
    def parse(self, itemName: str) -> EnchantmentAttribute:
        return {
            'Category': {
                'Name': _removeSymbol(itemName).replace('Max', 'M'),
                'IsPercentage': _findPercentage(itemName)
            },
            'Range': self.parseRange(itemName)
        }

class LongShortRangedPhysicalDamage(Parser):
    def match(self, itemName: str):
        return (itemName.find('遠距離') != -1 or itemName.find('近距離') != -1) and itemName.find('攻擊') != -1

    def parse(self, itemName: str) -> EnchantmentAttribute:
        if itemName.find('遠距離') != -1:
            name = '遠距離物理傷害'
        else:
            name = '近距離物理傷害'
        return {
            'Category': {
                'Name': name,
                'IsPercentage': True
            },
            'Range': self.parseRange(itemName)
        }

class MHPMSPParser(Parser):
    def match(self, itemName: str):
        return itemName.find('M') != -1 and (itemName.find('HP') != -1 or itemName.find('SP') != -1)

    def parse(self, itemName: str) -> EnchantmentAttribute:
        return {
            'Category': {
                'Name': _removeSymbol(itemName).replace('Max', 'M'),
                'IsPercentage': _findPercentage(itemName)
            },
            'Range': self.parseRange(itemName)
        }

class RecoveryParser(Parser):
    def match(self, itemName: str):
        return itemName.find('自然') != -1

    def parse(self, itemName: str) -> EnchantmentAttribute:
        return {
            'Category': {
                'Name': _removeSymbol(itemName).replace('恢復速度', '恢復量'),
                'IsPercentage': True
            },
            'Range': self.parseRange(itemName)
        }

class VariableCastTimeParser(Parser):
    def match(self, itemName: str):
        return itemName.find('變動') != -1 or itemName.find('變詠') != -1

    def parse(self, itemName: str) -> EnchantmentAttribute:
        return {
            'Category': {
                'Name': '變動詠唱時間',
                'IsPercentage': True
            },
            'Range': self.parseRange(itemName)
        }

class EnchantmentAttributeParser:
    def __init__(self):
        self.specialParsers = [
            CriticalDamageParser(),
            DelayAfterAttackParser(),
            DelayAfterSkillParser(),
            LongShortRangedPhysicalDamage(),
            MHPMSPParser(),
            RecoveryParser(),
            VariableCastTimeParser(),
        ]
        self.generalParser = GeneralParser()

    def parse(self, itemName: str) -> EnchantmentAttribute:
        for parser in self.specialParsers:
            if parser.match(itemName):
                return parser.parse(itemName)
        return self.generalParser.parse(itemName)
