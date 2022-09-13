import unittest
from simulate_enchanting.parser.category_parser import DelayAfterSkillParser

class TestDelayAfterSkillParser(unittest.TestCase):
    def testParse(self):
        parser = DelayAfterSkillParser()
        self.assertEqual(parser.parse('技能後延遲-1~5%'), { 'Name': '技能後延遲', 'IsPercentage': True })
        self.assertEqual(parser.parse('技能後延遲減少1~3%'), { 'Name': '技能後延遲', 'IsPercentage': True })
        self.assertEqual(parser.parse('技能的後延遲減少1~5%'), { 'Name': '技能後延遲', 'IsPercentage': True })

if __name__ == '__main__':
    unittest.main()