from simulate_enchanting.core import EnchantmentCategory

class GeneralParser:
    def parse(self, itemName: str) -> EnchantmentCategory:
        return {
            'Name': self.__removeSymbolAndDigit(itemName),
            'IsPercentage': '%' in set(itemName)
        }

    def __removeSymbolAndDigit(self, text: str):
        text = ''.join([i for i in text if not i.isdigit()])
        text = text.replace('+', '')
        text = text.replace('-', '')
        text = text.replace('%', '')
        text = text.replace('~', '')
        text = text.replace(' ', '')
        text = text.replace(',', '')
        return text