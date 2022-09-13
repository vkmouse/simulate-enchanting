import unittest
from simulate_enchanting.parser.row_parser import RowParser

class TestRowParser(unittest.TestCase):
    def testParse(self):
        parser = RowParser()
        self.assertTrue(parser.parse('---------------固定附加第一欄隨機能力---------------'), {
            'Probability': 1,
            'RowNumber': 1
        })
        self.assertTrue(parser.parse('---------------固定附加第二欄隨機能力---------------'), {
            'Probability': 1,
            'RowNumber': 2
        })
        self.assertTrue(parser.parse('---------------固定附加第三欄隨機能力---------------'), {
            'Probability': 1,
            'RowNumber': 3
        })
        self.assertTrue(parser.parse('---------------10%追加第二欄隨機能力---------------'), {
            'Probability': 0.1,
            'RowNumber': 2
        })
        self.assertTrue(parser.parse('---------------50%追加第三欄隨機能力---------------'), {
            'Probability': 0.5,
            'RowNumber': 3
        })

if __name__ == '__main__':
    unittest.main()