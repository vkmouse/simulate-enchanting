import unittest
from simulate_enchanting.parser.category_parser import CriticalDamageParser

class TestCriticalDamageParser(unittest.TestCase):
    def testParse(self):
        parser = CriticalDamageParser()
        self.assertEqual(parser.parse('必殺技傷害增加+1~5%'), { 'Name': '暴擊傷害', 'IsPercentage': True })

if __name__ == '__main__':
    unittest.main()