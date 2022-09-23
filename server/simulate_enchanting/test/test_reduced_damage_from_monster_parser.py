import unittest
from simulate_enchanting.parser.category_parser import ReducedDamageFromMonsterParser

class TestReducedDamageFromMonsterParser(unittest.TestCase):
    def testParse(self):
        parser = ReducedDamageFromMonsterParser()
        self.assertEqual(parser.parse('對小型魔物受到的物理攻擊減少1~3%'), { 'Name': '對小型魔物受到的物理攻擊', 'IsPercentage': True })
        self.assertEqual(parser.parse('遭受中型怪的魔法傷害減少 1,2%'), { 'Name': '遭受中型怪的魔法傷害', 'IsPercentage': True })
        self.assertEqual(parser.parse('受到近距離物理傷害減少1,2%'), { 'Name': '受到近距離物理傷害', 'IsPercentage': True })
        self.assertEqual(parser.parse('被無屬性魔物受到的物理傷害力減少 3~5%'), { 'Name': '被無屬性魔物受到的物理傷害力', 'IsPercentage': True })

if __name__ == '__main__':
    unittest.main()