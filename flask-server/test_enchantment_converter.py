import unittest
from core import EnchantmentProbabilityNotice
from enchantment_converter import EnchantmentProbabilityNoticeConverter

class TestEnchantmentProbabilityNoticeConverter(unittest.TestCase):
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
        converter = EnchantmentProbabilityNoticeConverter(self.notice)
        converter.convert()
        expected = {
            'Name': '影子技能屬性箱', 
            'Des': '能賦予影子技能系列的附加能力。 需+5以上限定道具才可使用。(附加能力後保留精煉值)', 
            'Url': 'https://ro.gnjoy.com.tw/notice/notice_view.aspx?id=175452',
            'API': 'https://ro.gnjoy.com.tw/notice/Scroll2/ScrollDetail2.ashx?SN=SkillShadowRanBox_TW&scrollID=1023'
        }
        self.assertDictEqual(converter.serial, expected)

    def testCategories(self):
        converter = EnchantmentProbabilityNoticeConverter(self.notice)
        converter.convert()
        expected = [
            { 'Name': '對無屬性攻擊的抗性', 'IsPercentage': True },
            { 'Name': '對風屬性攻擊的抗性', 'IsPercentage': True }
        ]
        self.assertListEqual(converter.categories, expected)

    def testRanges(self):
        converter = EnchantmentProbabilityNoticeConverter(self.notice)
        converter.convert()
        expected = [
            { 'Start': 1, 'Stop': 2, 'Step': 1 },
            { 'Start': 3, 'Stop': 5, 'Step': 2 }
        ]
        self.assertListEqual(converter.ranges, expected)

    def testRows(self):
        converter = EnchantmentProbabilityNoticeConverter(self.notice)
        converter.convert()
        expected = [{
            'Probability': 1,
            'RowNumber': 1,
        }, {
            'Probability': 0.1,
            'RowNumber': 2,
        }]
        self.assertListEqual(converter.rows, expected)

    def testAttributeProbabilities(self):
        converter = EnchantmentProbabilityNoticeConverter(self.notice)
        converter.convert()
        expected = [{  
            'Attribute': {
                'Category': { 'Name': '對無屬性攻擊的抗性', 'IsPercentage': True },
                'Range': { 'Start': 1, 'Stop': 2, 'Step': 1 },
            },
            'Probability': 0.045,
            'Row': {
                'Probability': 1,
                'RowNumber': 1,
            },
            'Serial': {
                'Name': '影子技能屬性箱', 
                'Des': '能賦予影子技能系列的附加能力。 需+5以上限定道具才可使用。(附加能力後保留精煉值)', 
                'Url': 'https://ro.gnjoy.com.tw/notice/notice_view.aspx?id=175452',
                'API': 'https://ro.gnjoy.com.tw/notice/Scroll2/ScrollDetail2.ashx?SN=SkillShadowRanBox_TW&scrollID=1023'
            }
        }, {
            'Attribute': {
                'Category': { 'Name': '對風屬性攻擊的抗性', 'IsPercentage': True },
                'Range': { 'Start': 1, 'Stop': 2, 'Step': 1 },
            },
            'Probability': 0.04,
            'Row': {
                'Probability': 1,
                'RowNumber': 1,
            },
            'Serial': {
                'Name': '影子技能屬性箱', 
                'Des': '能賦予影子技能系列的附加能力。 需+5以上限定道具才可使用。(附加能力後保留精煉值)', 
                'Url': 'https://ro.gnjoy.com.tw/notice/notice_view.aspx?id=175452',
                'API': 'https://ro.gnjoy.com.tw/notice/Scroll2/ScrollDetail2.ashx?SN=SkillShadowRanBox_TW&scrollID=1023'
            }
        }, {
            'Attribute': {
                'Category': { 'Name': '對風屬性攻擊的抗性', 'IsPercentage': True },
                'Range': { 'Start': 3, 'Stop': 5, 'Step': 2 },
            },
            'Probability': 0.0425,
            'Row': {
                'Probability': 0.1,
                'RowNumber': 2,
            },
            'Serial': {
                'Name': '影子技能屬性箱', 
                'Des': '能賦予影子技能系列的附加能力。 需+5以上限定道具才可使用。(附加能力後保留精煉值)', 
                'Url': 'https://ro.gnjoy.com.tw/notice/notice_view.aspx?id=175452',
                'API': 'https://ro.gnjoy.com.tw/notice/Scroll2/ScrollDetail2.ashx?SN=SkillShadowRanBox_TW&scrollID=1023'
            }
        }]
        self.assertListEqual(converter.attributeProbabilities, expected)

if __name__ == '__main__':
    unittest.main()