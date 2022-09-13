from simulate_enchanting.core import EnchantmentCategory
from simulate_enchanting.parser.category_parser import GeneralParser

class DelayAfterAttackParser(GeneralParser):
    def match(self, itemName: str):
        return itemName.find('攻擊後延遲') != -1
    
    def parse(self, itemName: str) -> EnchantmentCategory:
        result = super().parse(itemName)
        result['Name'] = '攻擊速度增加(攻擊後延遲)'
        return result