import unittest
from simulate_enchanting.parser.range_parser import RangeLexer

class TestRangeLexer(unittest.TestCase):
    def testGetNextToken(self):
        lexer = RangeLexer('攻擊速度增加(攻擊後延遲-%)1~5')
        self.assertEqual(lexer.getNextToken(), { 'Type': 'MINUS', 'Value': '-' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'INTEGER', 'Value': '1' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'TILDE', 'Value': '~' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'INTEGER', 'Value': '5' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'EOS', 'Value': '' })

        lexer = RangeLexer('減少攻擊後延遲1,3,5%')
        self.assertEqual(lexer.getNextToken(), { 'Type': 'MINUS', 'Value': '-' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'INTEGER', 'Value': '1' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'COMMA', 'Value': ',' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'INTEGER', 'Value': '3' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'COMMA', 'Value': ',' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'INTEGER', 'Value': '5' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'EOS', 'Value': '' })

        lexer = RangeLexer('減少攻擊後延遲15%')
        self.assertEqual(lexer.getNextToken(), { 'Type': 'MINUS', 'Value': '-' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'INTEGER', 'Value': '15' })
        self.assertEqual(lexer.getNextToken(), { 'Type': 'EOS', 'Value': '' })

        lexer = RangeLexer('武器不會被破壞')
        self.assertEqual(lexer.getNextToken(), { 'Type': 'EOS', 'Value': '' })

if __name__ == '__main__':
    unittest.main()