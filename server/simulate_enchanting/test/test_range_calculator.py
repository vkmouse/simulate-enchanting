import unittest
from simulate_enchanting.parser.range_parser import RangeCalculator

class TestRangeCalculator(unittest.TestCase):
    def testCalculateZeroRange(self):
        calculator = RangeCalculator()
        self.assertEqual(calculator.calculate(), { 'Start': 0, 'Stop': 0, 'Step': 1 })

    def testCalculateOneRange(self):
        calculator = RangeCalculator()
        calculator.append(5)
        self.assertEqual(calculator.calculate(), { 'Start': 5, 'Stop': 5, 'Step': 1 })

    def testCalculateRange(self):
        calculator = RangeCalculator()
        calculator.append(5)
        calculator.append(10)
        self.assertEqual(calculator.calculate(), { 'Start': 5, 'Stop': 10, 'Step': 1 })

    def testCalculateDiscreteRange(self):
        calculator = RangeCalculator()
        calculator.append(5)
        calculator.append(10)
        calculator.isDiscrete = True
        self.assertEqual(calculator.calculate(), { 'Start': 5, 'Stop': 10, 'Step': 5 })

    def testCalculateNegativeRange(self):
        calculator = RangeCalculator()
        calculator.append(5)
        calculator.append(10)
        calculator.isNegative = True
        self.assertEqual(calculator.calculate(), { 'Start': -10, 'Stop': -5, 'Step': 1 })

    def testCalculateNegativeAndDiscreteRange(self):
        calculator = RangeCalculator()
        calculator.append(5)
        calculator.append(10)
        calculator.isNegative = True
        calculator.isDiscrete = True
        self.assertEqual(calculator.calculate(), { 'Start': -10, 'Stop': -5, 'Step': 5 })

if __name__ == '__main__':
    unittest.main()