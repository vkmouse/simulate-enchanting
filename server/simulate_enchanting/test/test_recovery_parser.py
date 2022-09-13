import unittest
from simulate_enchanting.parser.category_parser import RecoveryParser

class TestRecoveryParser(unittest.TestCase):
    def testParse(self):
        parser = RecoveryParser()
        self.assertEqual(parser.parse('HP 自然恢復速度 + 5~10%'), { 'Name': 'HP自然恢復量', 'IsPercentage': True })
        self.assertEqual(parser.parse('HP自然恢復速度+5~10%'), { 'Name': 'HP自然恢復量', 'IsPercentage': True })
        self.assertEqual(parser.parse('HP自然恢復量+20%'), { 'Name': 'HP自然恢復量', 'IsPercentage': True })
        self.assertEqual(parser.parse('SP 自然恢復速度 + 5~10%'), { 'Name': 'SP自然恢復量', 'IsPercentage': True })
        self.assertEqual(parser.parse('SP自然恢復速度+5~10%'), { 'Name': 'SP自然恢復量', 'IsPercentage': True })
        self.assertEqual(parser.parse('SP自然恢復量+20%'), { 'Name': 'SP自然恢復量', 'IsPercentage': True })

if __name__ == '__main__':
    unittest.main()