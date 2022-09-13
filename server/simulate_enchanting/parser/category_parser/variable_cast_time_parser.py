from simulate_enchanting.core import EnchantmentCategory
from simulate_enchanting.parser.category_parser import GeneralParser

class VariableCastTimeParser(GeneralParser):
    def match(self, itemName: str):
        return itemName.find('變動') != -1 or itemName.find('變詠') != -1
    
    def parse(self, itemName: str) -> EnchantmentCategory:
        result = super().parse(itemName)
        result['Name'] = '變動詠唱時間'
        return result