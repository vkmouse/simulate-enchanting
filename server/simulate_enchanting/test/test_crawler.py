import unittest
from typing import List
from simulate_enchanting.core.notice import EnchantmentProbabilityNotice
from simulate_enchanting.crawler.crawler import EnchantmentProbabilityNoticeCrawler

class EnchantmentProbabilityNoticeCrawlerTest(unittest.TestCase):
    notices: List[EnchantmentProbabilityNotice] = [{ 
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
            'Value': '4.000%',
            'Memo': '',
            'Type': 1
        }],  
        'Des': '能賦予影子技能系列的附加能力。 需+5以上限定道具才可使用。(附加能力後保留精煉值)', 
        'Url': 'https://ro.gnjoy.com.tw/notice/notice_view.aspx?id=175452',
        'API': 'https://ro.gnjoy.com.tw/notice/Scroll2/ScrollDetail2.ashx?SN=SkillShadowRanBox_TW&scrollID=1023'
    }, {
        'Name': '時光斗篷寶箱', 
        'Items': [],
        'Des': '可獲得(力量、智慧、幸運、體力、敏捷、靈巧)時光斗篷裝備其中之一與其附魔道具。', 
        'Url': 'https://ro.gnjoy.com.tw/notice/notice_view.aspx?id=175413',
        'API': 'https://ro.gnjoy.com.tw/notice/Scroll2/ScrollDetail2.ashx?SN=Temporal_Box_TW&scrollID=1005'
    }]
    
    @unittest.skipIf(not EnchantmentProbabilityNoticeCrawler.isAvailable(),
        'Notice crawler is not available')
    def testRun(self):
        crawler = EnchantmentProbabilityNoticeCrawler()
        notice = crawler.run(self.notices[0]['Url'])

        self.assertEqual(notice['Name'], self.notices[0]['Name'])
        self.assertEqual(notice['Url'], self.notices[0]['Url'])
        self.assertEqual(notice['API'], self.notices[0]['API'])
        self.assertEqual(notice['Items'][0], self.notices[0]['Items'][0])

    @unittest.skipIf(not EnchantmentProbabilityNoticeCrawler.isAvailable(),
        'Notice crawler is not available')
    def testCheckNoticeTrue(self):
        crawler = EnchantmentProbabilityNoticeCrawler()
        notice = crawler.run(self.notices[0]['Url'])
        isEnchantmentProbabilityNotice = crawler.checkNotice(notice)

        self.assertEqual(notice['Name'], self.notices[0]['Name'])
        self.assertEqual(notice['Url'], self.notices[0]['Url'])
        self.assertEqual(notice['API'], self.notices[0]['API'])
        self.assertTrue(isEnchantmentProbabilityNotice)

    @unittest.skipIf(not EnchantmentProbabilityNoticeCrawler.isAvailable(),
        'Notice crawler is not available')
    def testCheckNoticeFalse(self):
        crawler = EnchantmentProbabilityNoticeCrawler()
        notice = crawler.run(self.notices[1]['Url'])
        isEnchantmentProbabilityNotice = crawler.checkNotice(notice)

        self.assertEqual(notice['Name'], self.notices[1]['Name'])
        self.assertEqual(notice['Url'], self.notices[1]['Url'])
        self.assertEqual(notice['API'], self.notices[1]['API'])
        self.assertFalse(isEnchantmentProbabilityNotice)

if __name__ == '__main__':
    unittest.main()