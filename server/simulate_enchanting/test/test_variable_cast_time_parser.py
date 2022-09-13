import unittest
from simulate_enchanting.parser.category_parser import VariableCastTimeParser

class TestVariableCastTimeParser(unittest.TestCase):
    def testParse(self):
        parser = VariableCastTimeParser()
        self.assertEqual(parser.parse('變動施法時間減少5~12%'), { 'Name': '變動詠唱時間', 'IsPercentage': True })
        self.assertEqual(parser.parse('變動詠唱-1~3%'), { 'Name': '變動詠唱時間', 'IsPercentage': True })
        self.assertEqual(parser.parse('變動詠唱減少5~8%'), { 'Name': '變動詠唱時間', 'IsPercentage': True })
        self.assertEqual(parser.parse('變詠時間 -1,2%'), { 'Name': '變動詠唱時間', 'IsPercentage': True })

if __name__ == '__main__':
    unittest.main()