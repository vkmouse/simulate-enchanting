from simulate_enchanting.core import EnchantmentCategory
from simulate_enchanting.parser.category_parser import GeneralParser

class ReducedDamageFromMonsterParser(GeneralParser):
    def match(self, itemName: str):
        isDamageFromMonster = (itemName.find('遭受') != -1 or itemName.find('受到') != -1)
        isReduced = itemName.find('減少') != -1
        return isReduced and isDamageFromMonster
    
    def parse(self, itemName: str) -> EnchantmentCategory:
        result = super().parse(itemName)
        result['Name'] = result['Name'].replace('減少', '')
        return result
