from simulate_enchanting.core import EnchantmentRange

class RangeCalculator:
    def __init__(self):
        self.__numbers = []
        self.isNegative = False
        self.isDiscrete = False

    def append(self, number: int):
        self.__numbers.append(number)
    
    def calculate(self) -> EnchantmentRange:
        output: EnchantmentRange = { 'Start': 0, 'Stop': 0, 'Step': 1 }
        if len(self.__numbers) > 0:
            output['Start'] = self.__numbers[0]
            output['Stop'] = self.__numbers[-1]
        if self.isDiscrete:
            output['Step'] = self.__numbers[1] - self.__numbers[0]
            for i in range(len(self.__numbers) - 1):
                if self.__numbers[i] + output['Step'] != self.__numbers[i + 1]:
                    raise Exception('numbersToRange failed')
        if self.isNegative:
            output['Start'], output['Stop'] = -output['Stop'], -output['Start']
        return output