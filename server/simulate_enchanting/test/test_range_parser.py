import unittest
from simulate_enchanting.parser.range_parser import RangeParser

class TestRangeParser(unittest.TestCase):
    def testParse(self):
        parser = RangeParser()
        self.assertEqual(parser.parse('攻擊速度增加(攻擊後延遲-%)1~5'), { 'Start': -5, 'Stop': -1, 'Step': 1 })
        self.assertEqual(parser.parse('減少攻擊後延遲1,3,5%'), { 'Start': -5, 'Stop': -1, 'Step': 2 })
        self.assertEqual(parser.parse('減少攻擊後延遲15%'), { 'Start': -15, 'Stop': -15, 'Step': 1 })
        self.assertEqual(parser.parse('HP自然恢復量+1~5%'), { 'Start': 1, 'Stop': 5, 'Step': 1 })
        self.assertEqual(parser.parse('HP自然恢復量+10,20%'), { 'Start': 10, 'Stop': 20, 'Step': 10 })
        self.assertEqual(parser.parse('HP自然恢復量+1,3,5%'), { 'Start': 1, 'Stop': 5, 'Step': 2 })
        self.assertEqual(parser.parse('HP自然恢復量+15%'), { 'Start': 15, 'Stop': 15, 'Step': 1 })
        self.assertEqual(parser.parse('武器不會被破壞'), { 'Start': 0, 'Stop': 0, 'Step': 1 })

if __name__ == '__main__':
    unittest.main()