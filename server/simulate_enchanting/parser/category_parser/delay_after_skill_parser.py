from simulate_enchanting.core import EnchantmentCategory
from simulate_enchanting.parser.category_parser import GeneralParser

class DelayAfterSkillParser(GeneralParser):
    def match(self, itemName: str):
        return itemName.find('技能') != -1 and itemName.find('後延遲') != -1
    
    def parse(self, itemName: str) -> EnchantmentCategory:
        result = super().parse(itemName)
        result['Name'] = '技能後延遲'
        return result