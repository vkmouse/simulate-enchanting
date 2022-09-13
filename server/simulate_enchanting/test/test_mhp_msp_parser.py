import unittest
from simulate_enchanting.parser.category_parser import MHPMSPParser

class TestMHPMSPParser(unittest.TestCase):
    def testParse(self):
        parser = MHPMSPParser()
        self.assertEqual(parser.parse('MaxHP+1%'), { 'Name': 'MHP', 'IsPercentage': True })
        self.assertEqual(parser.parse('MaxHP+10~15%'), { 'Name': 'MHP', 'IsPercentage': True })
        self.assertEqual(parser.parse('MHP + 1~2%'), { 'Name': 'MHP', 'IsPercentage': True })
        self.assertEqual(parser.parse('MHP+1~5%'), { 'Name': 'MHP', 'IsPercentage': True })

        self.assertEqual(parser.parse('MHP + 200'), { 'Name': 'MHP', 'IsPercentage': False })
        self.assertEqual(parser.parse('MHP+500~1000'), { 'Name': 'MHP', 'IsPercentage': False })
        self.assertEqual(parser.parse('MaxHP+100~500'), { 'Name': 'MHP', 'IsPercentage': False })
        self.assertEqual(parser.parse('MHP + 200,40'), { 'Name': 'MHP', 'IsPercentage': False })
        
        self.assertEqual(parser.parse('MSP+1~5%'), { 'Name': 'MSP', 'IsPercentage': True })
        self.assertEqual(parser.parse('MaxSP+1%'), { 'Name': 'MSP', 'IsPercentage': True })
        self.assertEqual(parser.parse('MaxSP+1~3%'), { 'Name': 'MSP', 'IsPercentage': True })
        self.assertEqual(parser.parse('MSP + 1~2%'), { 'Name': 'MSP', 'IsPercentage': True })

        self.assertEqual(parser.parse('MSP + 25,50'), { 'Name': 'MSP', 'IsPercentage': False })
        self.assertEqual(parser.parse('MSP + 25'), { 'Name': 'MSP', 'IsPercentage': False })
        self.assertEqual(parser.parse('MSP+50~1000'), { 'Name': 'MSP', 'IsPercentage': False })
        self.assertEqual(parser.parse('MaxSP+20~100'), { 'Name': 'MSP', 'IsPercentage': False })

if __name__ == '__main__':
    unittest.main()