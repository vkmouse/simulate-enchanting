from simulate_enchanting.core import EnchantmentCategory
from simulate_enchanting.parser.category_parser import GeneralParser

class CriticalDamageParser(GeneralParser):
    def match(self, itemName: str):
        return itemName.find('必殺技傷害增加') != -1
    
    def parse(self, itemName: str) -> EnchantmentCategory:
        result = super().parse(itemName)
        result['Name'] = '暴擊傷害'
        return result