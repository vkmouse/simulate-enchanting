from simulate_enchanting.core import EnchantmentCategory
from simulate_enchanting.parser.category_parser import GeneralParser

class RecoveryParser(GeneralParser):
    def match(self, itemName: str):
        return itemName.find('自然') != -1
    
    def parse(self, itemName: str) -> EnchantmentCategory:
        result = super().parse(itemName)
        result['Name'] = result['Name'].replace('恢復速度', '恢復量')
        return result