from simulate_enchanting.core import EnchantmentCategory
from simulate_enchanting.parser.category_parser import GeneralParser

class ReducedSpParser(GeneralParser):
    def match(self, itemName: str):
        isSp = itemName.find('SP消耗') != -1
        isReduced = itemName.find('減少') != -1
        return isReduced and isSp
    
    def parse(self, itemName: str) -> EnchantmentCategory:
        result = super().parse(itemName)
        result['Name'] = result['Name'].replace('減少', '')
        return result
