from simulate_enchanting.core import EnchantmentRange
from simulate_enchanting.parser.range_parser import RangeCalculator
from simulate_enchanting.parser.range_parser import RangeLexer

class RangeParser:
    def parse(self, itemName: str) -> EnchantmentRange:
        self.__lexer = RangeLexer(itemName)
        self.__currentToken = self.__lexer.getNextToken()
        self.__rangeNode = RangeCalculator()
        self.__expr()
        return self.__rangeNode.calculate()

    def __expr(self):
        if self.__currentType == 'EOS':
            self.__eat('EOS')
        else:
            if self.__currentType == 'MINUS':
                self.__eat('MINUS')
                self.__rangeNode.isNegative = True
            self.__term()

    def __term(self):
        self.__factor()
        if self.__currentType == 'TILDE':
            self.__eat('TILDE')
            self.__factor()
        else:
            while self.__currentType == 'COMMA':
                self.__rangeNode.isDiscrete = True
                self.__eat('COMMA')
                self.__factor()

    def __factor(self):
        self.__rangeNode.append(int(self.__currentToken['Value']))
        self.__eat('INTEGER')

    def __eat(self, Type):
        if self.__currentType == Type:
            self.__currentToken = self.__lexer.getNextToken()
        else:
            raise Exception('Invalid syntax')

    @property
    def __currentType(self):
        return self.__currentToken['Type']
