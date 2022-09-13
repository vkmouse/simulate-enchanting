import unittest
from simulate_enchanting.core import EnchantmentProbabilityNotice
from simulate_enchanting.parser import Parser

class TestCriticalDamageParser(unittest.TestCase):
    notice: EnchantmentProbabilityNotice = { 
        'Name': '影子技能屬性箱', 
        'Items': [{ 
            'Name': '---------------固定附加第一欄隨機能力---------------',
            'Count': 0,
            'Value': '', 
            'Memo': '',
            'Type': 1 
        }, { 
            'Name': '對無屬性攻擊的抗性+1~2%',
            'Count': 0,
            'Value': '4.500%',
            'Memo': '',
            'Type': 1
        }, { 
            'Name': '對風屬性攻擊的抗性+1~2%',
            'Count': 0,
            'Value': '4.000%',
            'Memo': '',
            'Type': 1
        }, {
            'Name': '---------------10%追加第二欄隨機能力---------------',
            'Count': 0,
            'Value': '',
            'Memo': '',
            'Type': 1
        }, { 
            'Name': '對風屬性攻擊的抗性+3,5%',
            'Count': 0,
            'Value': '4.250%',
            'Memo': '',
            'Type': 1
        }],  
        'Des': '能賦予影子技能系列的附加能力。 需+5以上限定道具才可使用。(附加能力後保留精煉值)', 
        'Url': 'https://ro.gnjoy.com.tw/notice/notice_view.aspx?id=175452',
        'API': 'https://ro.gnjoy.com.tw/notice/Scroll2/ScrollDetail2.ashx?SN=SkillShadowRanBox_TW&scrollID=1023'
    }

    def testSerial(self):
        parser = Parser()
        parseResult = parser.parse(self.notice)
        expected = {
            'Name': '影子技能屬性箱', 
            'Des': '能賦予影子技能系列的附加能力。 需+5以上限定道具才可使用。(附加能力後保留精煉值)', 
            'Url': 'https://ro.gnjoy.com.tw/notice/notice_view.aspx?id=175452',
            'API': 'https://ro.gnjoy.com.tw/notice/Scroll2/ScrollDetail2.ashx?SN=SkillShadowRanBox_TW&scrollID=1023'
        }
        self.assertDictEqual(parseResult['Serial'], expected)

    def testCategories(self):
        parser = Parser()
        parseResult = parser.parse(self.notice)
        expected = [
            { 'Name': '對無屬性攻擊的抗性', 'IsPercentage': True },
            { 'Name': '對風屬性攻擊的抗性', 'IsPercentage': True }
        ]
        self.assertListEqual(parseResult['Categories'], expected)

    def testRanges(self):
        parser = Parser()
        parseResult = parser.parse(self.notice)
        expected = [
            { 'Start': 1, 'Stop': 2, 'Step': 1 },
            { 'Start': 3, 'Stop': 5, 'Step': 2 }
        ]
        self.assertListEqual(parseResult['Ranges'], expected)

    def testRows(self):
        parser = Parser()
        parseResult = parser.parse(self.notice)
        expected = [{
            'Probability': 1,
            'RowNumber': 1,
        }, {
            'Probability': 0.1,
            'RowNumber': 2,
        }]
        self.assertListEqual(parseResult['Rows'], expected)

    def testAttributeProbabilities(self):
        parser = Parser()
        parseResult = parser.parse(self.notice)
        expected = [{  
            'Probability': 0.045,
            'Category': { 'Name': '對無屬性攻擊的抗性', 'IsPercentage': True },
            'Range': { 'Start': 1, 'Stop': 2, 'Step': 1 },
            'Row': { 'Probability': 1, 'RowNumber': 1 },
            'Serial': {
                'Name': '影子技能屬性箱', 
                'Des': '能賦予影子技能系列的附加能力。 需+5以上限定道具才可使用。(附加能力後保留精煉值)', 
                'Url': 'https://ro.gnjoy.com.tw/notice/notice_view.aspx?id=175452',
                'API': 'https://ro.gnjoy.com.tw/notice/Scroll2/ScrollDetail2.ashx?SN=SkillShadowRanBox_TW&scrollID=1023'
            }
        }, {
            'Probability': 0.04,
            'Category': { 'Name': '對風屬性攻擊的抗性', 'IsPercentage': True },
            'Range': { 'Start': 1, 'Stop': 2, 'Step': 1 },
            'Row': { 'Probability': 1, 'RowNumber': 1 },
            'Serial': {
                'Name': '影子技能屬性箱', 
                'Des': '能賦予影子技能系列的附加能力。 需+5以上限定道具才可使用。(附加能力後保留精煉值)', 
                'Url': 'https://ro.gnjoy.com.tw/notice/notice_view.aspx?id=175452',
                'API': 'https://ro.gnjoy.com.tw/notice/Scroll2/ScrollDetail2.ashx?SN=SkillShadowRanBox_TW&scrollID=1023'
            }
        }, {
            'Probability': 0.0425,
            'Category': { 'Name': '對風屬性攻擊的抗性', 'IsPercentage': True },
            'Range': { 'Start': 3, 'Stop': 5, 'Step': 2 },
            'Row': { 'Probability': 0.1, 'RowNumber': 2 },
            'Serial': {
                'Name': '影子技能屬性箱', 
                'Des': '能賦予影子技能系列的附加能力。 需+5以上限定道具才可使用。(附加能力後保留精煉值)', 
                'Url': 'https://ro.gnjoy.com.tw/notice/notice_view.aspx?id=175452',
                'API': 'https://ro.gnjoy.com.tw/notice/Scroll2/ScrollDetail2.ashx?SN=SkillShadowRanBox_TW&scrollID=1023'
            }
        }]
        self.assertListEqual(parseResult['Attributes'], expected)

if __name__ == '__main__':
    unittest.main()