import unittest
from simulate_enchanting.parser.category_parser import LongShortRangedPhysicalDamageParser

class TestLongShortRangedPhysicalDamageParser(unittest.TestCase):
    def testParse(self):
        parser = LongShortRangedPhysicalDamageParser()
        self.assertEqual(parser.parse('遠距離攻擊增加+1~5%'), { 'Name': '遠距離物理傷害', 'IsPercentage': True })
        self.assertEqual(parser.parse('遠距離攻擊增加1~5%'), { 'Name': '遠距離物理傷害', 'IsPercentage': True })
        self.assertEqual(parser.parse('遠距離物理傷害 + 1,2%'), { 'Name': '遠距離物理傷害', 'IsPercentage': True })
        self.assertEqual(parser.parse('遠距離物理傷害+1~5%'), { 'Name': '遠距離物理傷害', 'IsPercentage': True })
        self.assertEqual(parser.parse('遠距離物理攻擊傷害+1~5%'), { 'Name': '遠距離物理傷害', 'IsPercentage': True })
        self.assertEqual(parser.parse('近距離物理攻擊傷害+1~5%'), { 'Name': '近距離物理傷害', 'IsPercentage': True })

if __name__ == '__main__':
    unittest.main()


