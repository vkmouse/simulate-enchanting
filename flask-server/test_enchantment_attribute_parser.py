from unicodedata import category
import unittest
from enchantment_attribute_parser import EnchantmentAttributeParser, RangeLexer, RangeParser

class TestRangeLexer(unittest.TestCase):
    def testGetNextToken(self):
        lexer = RangeLexer('攻擊速度增加(攻擊後延遲-%)1~5')
        self.assertEqual(lexer.getNextToken(), { 'Type': 'MINUS', 'Value': '-' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'INTEGER', 'Value': '1' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'TILDE', 'Value': '~' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'INTEGER', 'Value': '5' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'EOS', 'Value': '' })

        lexer = RangeLexer('減少攻擊後延遲1,3,5%')
        self.assertEqual(lexer.getNextToken(), { 'Type': 'MINUS', 'Value': '-' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'INTEGER', 'Value': '1' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'COMMA', 'Value': ',' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'INTEGER', 'Value': '3' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'COMMA', 'Value': ',' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'INTEGER', 'Value': '5' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'EOS', 'Value': '' })

        lexer = RangeLexer('減少攻擊後延遲15%')
        self.assertEqual(lexer.getNextToken(), { 'Type': 'MINUS', 'Value': '-' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'INTEGER', 'Value': '15' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'EOS', 'Value': '' })

        lexer = RangeLexer('武器不會被破壞')
        self.assertEqual(lexer.getNextToken(), { 'Type': 'EOS', 'Value': '' })

class TestRangeParser(unittest.TestCase):
    def testParse(self):
        parser = RangeParser('攻擊速度增加(攻擊後延遲-%)1~5')
        self.assertEqual(parser.parse(), { 'Start': -5, 'Stop': -1, 'Step': 1 })
        parser = RangeParser('減少攻擊後延遲1,3,5%')
        self.assertEqual(parser.parse(), { 'Start': -5, 'Stop': -1, 'Step': 2 })
        parser = RangeParser('減少攻擊後延遲15%')
        self.assertEqual(parser.parse(), { 'Start': -15, 'Stop': -15, 'Step': 1 })
        parser = RangeParser('HP自然恢復量+1~5%')
        self.assertEqual(parser.parse(), { 'Start': 1, 'Stop': 5, 'Step': 1 })
        parser = RangeParser('HP自然恢復量+10,20%')
        self.assertEqual(parser.parse(), { 'Start': 10, 'Stop': 20, 'Step': 10 })
        parser = RangeParser('HP自然恢復量+1,3,5%')
        self.assertEqual(parser.parse(), { 'Start': 1, 'Stop': 5, 'Step': 2 })
        parser = RangeParser('HP自然恢復量+15%')
        self.assertEqual(parser.parse(), { 'Start': 15, 'Stop': 15, 'Step': 1 })
        parser = RangeParser('武器不會被破壞')
        self.assertEqual(parser.parse(), { 'Start': 0, 'Stop': 0, 'Step': 1 })

class TestEnchantmentAttributeParser(unittest.TestCase):
    dataset = [{
        'Category': {
            'Name': '攻擊速度增加(攻擊後延遲)',
            'IsPercentage': True
        }, 
        'Dataset': [
            { 'Name': '攻擊速度增加(攻擊後延遲-%)1~5', 'Start': -5, 'Stop': -1, 'Step': 1 },
            { 'Name': '攻擊速度增加(攻擊後延遲-1~5%)', 'Start': -5, 'Stop': -1, 'Step': 1 },
            { 'Name': '攻擊速度增加(攻擊後延遲減少%)1~5%', 'Start': -5, 'Stop': -1, 'Step': 1 },
            { 'Name': '減少攻擊後延遲1~5%', 'Start': -5, 'Stop': -1, 'Step': 1 },
            { 'Name': '減少攻擊後延遲1,2%', 'Start': -2, 'Stop': -1, 'Step': 1 },
            { 'Name': '攻擊速度增加(攻擊後延遲-3%)', 'Start': -3, 'Stop': -3, 'Step': 1 },
        ]
    }, {
        'Category': {
            'Name': '技能後延遲',
            'IsPercentage': True
        },
        'Dataset': [
            { 'Name': '技能後延遲-1~5%', 'Start': -5, 'Stop': -1, 'Step': 1 },
            { 'Name': '技能後延遲減少1~3%', 'Start': -3, 'Stop': -1, 'Step': 1 },
            { 'Name': '技能的後延遲減少1~5%', 'Start': -5, 'Stop': -1, 'Step': 1 },
        ]
    }, {
        'Category': {
            'Name': 'HP自然恢復量',
            'IsPercentage': True
        },
        'Dataset': [
            { 'Name': 'HP 自然恢復速度 + 5~10%', 'Start': 5,'Stop': 10, 'Step': 1 },
            { 'Name': 'HP自然恢復速度+5~10%', 'Start': 5,'Stop': 10, 'Step': 1 },
            { 'Name': 'HP自然恢復量+20%', 'Start': 20,'Stop': 20, 'Step': 1 },
        ]
    }, {
        'Category': {
            'Name': 'SP自然恢復量',
            'IsPercentage': True
        },
        'Dataset': [
            { 'Name': 'SP 自然恢復速度 + 5~10%', 'Start': 5,'Stop': 10, 'Step': 1 },
            { 'Name': 'SP自然恢復速度+5~10%', 'Start': 5,'Stop': 10, 'Step': 1 },
            { 'Name': 'SP自然恢復量+20%', 'Start': 20,'Stop': 20, 'Step': 1 },
        ]
    }, {
        'Category': {
            'Name': 'MHP',
            'IsPercentage': True
        },
        'Dataset': [
            { 'Name': 'MaxHP+1%', 'Start': 1,'Stop': 1, 'Step': 1 },
            { 'Name': 'MaxHP+10~15%', 'Start': 10,'Stop': 15, 'Step': 1 },
            { 'Name': 'MHP + 1~2%', 'Start': 1,'Stop': 2, 'Step': 1 },
            { 'Name': 'MHP+1~5%', 'Start': 1,'Stop': 5, 'Step': 1 },
        ]
    }, {
        'Category': {
            'Name': 'MHP',
            'IsPercentage': False
        },
        'Dataset':  [
            { 'Name': 'MHP + 200', 'Start': 200,'Stop': 200, 'Step': 1 },
            { 'Name': 'MHP+500~1000', 'Start': 500,'Stop': 1000, 'Step': 1 },
            { 'Name': 'MaxHP+100~500', 'Start': 100,'Stop': 500, 'Step': 1 },
        ]
    }, {
        'Category': {
            'Name': 'MSP',
            'IsPercentage': True
        },
        'Dataset':  [
            { 'Name': 'MSP+1~5%', 'Start': 1,'Stop': 5, 'Step': 1 },
            { 'Name': 'MaxSP+1%', 'Start': 1,'Stop': 1, 'Step': 1 },
            { 'Name': 'MaxSP+1~3%', 'Start': 1,'Stop': 3, 'Step': 1 },
            { 'Name': 'MSP + 1~2%', 'Start': 1,'Stop': 2, 'Step': 1 },
        ]
    }, {
        'Category': {
            'Name': 'MSP',
            'IsPercentage': False
        },
        'Dataset':  [
            { 'Name': 'MSP + 25', 'Start': 25,'Stop': 25, 'Step': 1 },
            { 'Name': 'MSP+50~1000', 'Start': 50,'Stop': 1000, 'Step': 1 },
            { 'Name': 'MaxSP+20~100', 'Start': 20,'Stop': 100, 'Step': 1 },
        ]
    }, {
        'Category': {
            'Name': '變動詠唱時間',
            'IsPercentage': True
        },
        'Dataset':  [
            { 'Name': '變動施法時間減少5~12%', 'Start': -12, 'Stop': -5, 'Step': 1 },
            { 'Name': '變動詠唱-1~3%', 'Start': -3, 'Stop': -1, 'Step': 1 },
            { 'Name': '變動詠唱減少5~8%', 'Start': -8, 'Stop': -5, 'Step': 1 },
            { 'Name': '變詠時間 -1,2%', 'Start': -2, 'Stop': -1, 'Step': 1 },
        ]
    }, {
        'Category': {
            'Name': 'MHP',
            'IsPercentage': False
        },
        'Dataset':  [
            { 'Name': 'MHP + 200,400', 'Start': 200, 'Stop': 400, 'Step': 200 }
        ]
    }, {
        'Category': {
            'Name': 'MSP',
            'IsPercentage': False
        },
        'Dataset':  [
            { 'Name': 'MSP + 25,50', 'Start': 25, 'Stop': 50, 'Step': 25 }
        ]
    }, {
        'Category': {
            'Name': 'ATK',
            'IsPercentage': True
        },
        'Dataset':  [
            { 'Name': 'ATK  + 1%', 'Start': 1, 'Stop': 1, 'Step': 1 },
            { 'Name': 'ATK + 1~3%', 'Start': 1, 'Stop': 3, 'Step': 1 },
            { 'Name': 'ATK +  1,3%', 'Start': 1, 'Stop': 3, 'Step': 2 }
        ]
    }, {
        'Category': {
            'Name': 'ATK',
            'IsPercentage': False
        },
        'Dataset':  [
            { 'Name': 'ATK  + 1', 'Start': 1, 'Stop': 1, 'Step': 1 },
            { 'Name': 'ATK + 1~3', 'Start': 1, 'Stop': 3, 'Step': 1 },
            { 'Name': 'ATK +  1,3', 'Start': 1, 'Stop': 3, 'Step': 2 }
        ]
    }, {
        'Category': {
            'Name': '不可破壞',
            'IsPercentage': False
        },
        'Dataset':  [
            { 'Name': '不可破壞', 'Start': 0, 'Stop': 0, 'Step': 1 },
        ]
    }, {
        'Category': {
            'Name': '遠距離物理傷害',
            'IsPercentage': True
        },
        'Dataset':  [
            { 'Name': '遠距離攻擊增加+1~5%', 'Start': 1, 'Stop': 5, 'Step': 1 },
            { 'Name': '遠距離攻擊增加1~5%', 'Start': 1, 'Stop': 5, 'Step': 1 },
            { 'Name': '遠距離物理傷害 + 1,2%', 'Start': 1, 'Stop': 2, 'Step': 1 },
            { 'Name': '遠距離物理傷害+1~5%', 'Start': 1, 'Stop': 5, 'Step': 1 },
            { 'Name': '遠距離物理攻擊傷害+1~5%', 'Start': 1, 'Stop': 5, 'Step': 1 },
        ]
    }, {
        'Category': {
            'Name': '近距離物理傷害',
            'IsPercentage': True
        },
        'Dataset':  [
            { 'Name': '近距離物理攻擊傷害+1~5%', 'Start': 1, 'Stop': 5, 'Step': 1 },
        ]
    }, {
        'Category': {
            'Name': '暴擊傷害',
            'IsPercentage': True
        },
        'Dataset':  [
            { 'Name': '暴擊傷害+1~5%', 'Start': 1, 'Stop': 5, 'Step': 1 },
            { 'Name': '必殺技傷害增加+1~5%', 'Start': 1, 'Stop': 5, 'Step': 1 },
        ]
    }, 

    ]

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.parser = EnchantmentAttributeParser()

    def testDataset(self):
        for ds in self.dataset:
            for data in ds['Dataset']:
                attribute = self.parser.parse(data['Name'])
                self.assertEqual(attribute, {
                    'Category': ds['Category'],
                    'Range': {
                        'Start': data['Start'],
                        'Stop': data['Stop'],
                        'Step': data['Step'],
                    }
                })


if __name__ == '__main__':
    unittest.main()