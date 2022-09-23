import unittest
from simulate_enchanting.parser.category_parser import ReducedSpParser

class TestReducedSpParser(unittest.TestCase):
    def testParse(self):
        parser = ReducedSpParser()
        self.assertEqual(parser.parse('使用技能SP消耗減少 1~3%'), { 'Name': '使用技能SP消耗', 'IsPercentage': True })
        self.assertEqual(parser.parse('使用技能SP消耗減少 1,2%'), { 'Name': '使用技能SP消耗', 'IsPercentage': True })

if __name__ == '__main__':
    unittest.main()