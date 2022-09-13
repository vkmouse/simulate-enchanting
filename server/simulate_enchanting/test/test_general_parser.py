import unittest
from simulate_enchanting.parser.category_parser import GeneralParser

class TestGeneralParser(unittest.TestCase):
    def testParse(self):
        parser = GeneralParser()
        self.assertEqual(parser.parse('暴擊傷害+1~5%'), { 'Name': '暴擊傷害', 'IsPercentage': True })
        self.assertEqual(parser.parse('不可破壞'), { 'Name': '不可破壞', 'IsPercentage': False })
        self.assertEqual(parser.parse('ATK  + 1'), { 'Name': 'ATK', 'IsPercentage': False })
        self.assertEqual(parser.parse('ATK + 1~3'), { 'Name': 'ATK', 'IsPercentage': False })
        self.assertEqual(parser.parse('ATK +  1,3'), { 'Name': 'ATK', 'IsPercentage': False })

if __name__ == '__main__':
    unittest.main()