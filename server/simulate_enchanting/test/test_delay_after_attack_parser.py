import unittest
from simulate_enchanting.parser.category_parser import DelayAfterAttackParser

class TestDelayAfterAttackParser(unittest.TestCase):
    def testParse(self):
        parser = DelayAfterAttackParser()
        self.assertEqual(parser.parse('攻擊速度增加(攻擊後延遲-%)1~5'), { 'Name': '攻擊速度增加(攻擊後延遲)', 'IsPercentage': True })
        self.assertEqual(parser.parse('攻擊速度增加(攻擊後延遲-1~5%)'), { 'Name': '攻擊速度增加(攻擊後延遲)', 'IsPercentage': True })
        self.assertEqual(parser.parse('攻擊速度增加(攻擊後延遲減少%)1~5%'), { 'Name': '攻擊速度增加(攻擊後延遲)', 'IsPercentage': True })
        self.assertEqual(parser.parse('減少攻擊後延遲1~5%'), { 'Name': '攻擊速度增加(攻擊後延遲)', 'IsPercentage': True })
        self.assertEqual(parser.parse('減少攻擊後延遲1,2%'), { 'Name': '攻擊速度增加(攻擊後延遲)', 'IsPercentage': True })
        self.assertEqual(parser.parse('攻擊速度增加(攻擊後延遲-3%)'), { 'Name': '攻擊速度增加(攻擊後延遲)', 'IsPercentage': True })

if __name__ == '__main__':
    unittest.main()