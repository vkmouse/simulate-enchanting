from simulate_enchanting.core import EnchantmentCategory
from simulate_enchanting.parser.category_parser import GeneralParser

class MHPMSPParser(GeneralParser):
    def match(self, itemName: str):
        return itemName.find('M') != -1 and (itemName.find('HP') != -1 or itemName.find('SP') != -1)
    
    def parse(self, itemName: str) -> EnchantmentCategory:
        result = super().parse(itemName)
        result['Name'] = result['Name'].replace('Max', 'M')
        return result