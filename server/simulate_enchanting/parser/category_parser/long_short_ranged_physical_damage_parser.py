from simulate_enchanting.core import EnchantmentCategory
from simulate_enchanting.parser.category_parser import GeneralParser

class LongShortRangedPhysicalDamageParser(GeneralParser):
    def match(self, itemName: str):
        return (itemName.find('遠距離') != -1 or itemName.find('近距離') != -1) and itemName.find('攻擊') != -1
    
    def parse(self, itemName: str) -> EnchantmentCategory:
        result = super().parse(itemName)
        if itemName.find('遠距離') != -1:
            result['Name'] = '遠距離物理傷害'
        else:
            result['Name'] = '近距離物理傷害'
        return result