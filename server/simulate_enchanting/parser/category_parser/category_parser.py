from simulate_enchanting.core import EnchantmentCategory
from simulate_enchanting.parser.category_parser import CriticalDamageParser
from simulate_enchanting.parser.category_parser import DelayAfterAttackParser
from simulate_enchanting.parser.category_parser import DelayAfterSkillParser
from simulate_enchanting.parser.category_parser import GeneralParser
from simulate_enchanting.parser.category_parser import LongShortRangedPhysicalDamageParser
from simulate_enchanting.parser.category_parser import MHPMSPParser
from simulate_enchanting.parser.category_parser import RecoveryParser
from simulate_enchanting.parser.category_parser import VariableCastTimeParser

class CategoryParser:
    def __init__(self):
        self.__matchableParsers = [
            CriticalDamageParser(),
            DelayAfterAttackParser(),
            DelayAfterSkillParser(),
            LongShortRangedPhysicalDamageParser(),
            MHPMSPParser(),
            RecoveryParser(),
            VariableCastTimeParser(),
        ]
        self.__generalParser = GeneralParser()

    def parse(self, itemName: str) -> EnchantmentCategory:
        for parser in self.__matchableParsers:
            if parser.match(itemName):
                return parser.parse(itemName)
        return self.__generalParser.parse(itemName)
