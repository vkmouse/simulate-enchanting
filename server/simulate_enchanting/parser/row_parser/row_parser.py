from simulate_enchanting.core import EnchantmentRow

class RowParser:
    def parse(self, itemName: str) -> EnchantmentRow:
        return {
            'Probability': self.__parseProbability(itemName),
            'RowNumber': self.__parseRowNumber(itemName),
        }

    def __parseRowNumber(self, itemName: str):
        if itemName.find('第一欄') != -1:
            return 1
        elif itemName.find('第二欄') != -1:
            return 2
        elif itemName.find('第三欄') != -1:
            return 3
        elif itemName.find('第四欄') != -1:
            return 4
        else:
            return -1
    
    def __parseProbability(self, itemName: str):
        num = ''.join([i for i in itemName if i.isdigit()])
        if len(num) == 0:
            return 1
        else:
            return int(num) / 100