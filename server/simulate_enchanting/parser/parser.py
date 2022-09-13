from typing import TypedDict, List
from simulate_enchanting.core import EnchantableAttribute, EnchantmentCategory, EnchantmentRange, EnchantmentRow, EnchantmentSerial, EnchantmentProbabilityNotice, EnchantmentProbabilityNoticeItem
from simulate_enchanting.parser.category_parser import CategoryParser
from simulate_enchanting.parser.range_parser import RangeParser
from simulate_enchanting.parser.row_parser import RowParser

class ParserResult(TypedDict):
    Attributes: List[EnchantableAttribute]
    Categories: List[EnchantmentCategory]
    Ranges: List[EnchantmentRange]
    Rows: List[EnchantmentRow]
    Serial: EnchantmentSerial

class Parser:
    def parse(self, notice: EnchantmentProbabilityNotice) -> ParserResult:
        return {
            'Attributes': self.__parseAttributes(notice),
            'Categories': self.__parseCategories(notice),
            'Ranges': self.__parseRanges(notice),
            'Rows': self.__parseRows(notice),
            'Serial': self.__parseSerial(notice)
        }

    def __parseAttributes(self, notice: EnchantmentProbabilityNotice) -> List[EnchantableAttribute]:
        categoryParser = CategoryParser()
        rangeParser = RangeParser()
        rowParser = RowParser()
        attributes: List[EnchantableAttribute] = []
        serial = self.__parseSerial(notice)
        row = None
        for item in notice['Items']:
            if self.__isCategory(item):
                attributes.append({
                    'Probability': self.__parseProbability(item['Value']),
                    'Category': categoryParser.parse(item['Name']),
                    'Range': rangeParser.parse(item['Name']),
                    'Row': row,
                    'Serial': serial
                })
            else:
                row = rowParser.parse(item['Name'])
        return attributes

    def __parseCategories(self, notice: EnchantmentProbabilityNotice) -> List[EnchantmentCategory]:
        parser = CategoryParser()
        items = filter(lambda item: self.__isCategory(item), notice['Items'])
        items = map(lambda item: parser.parse(item['Name']), items)
        results = []
        [results.append(x) for x in items if x not in results]
        return results

    def __parseRanges(self, notice: EnchantmentProbabilityNotice) -> List[EnchantmentRange]:
        parser = RangeParser()
        items = filter(lambda item: self.__isCategory(item), notice['Items'])
        items = map(lambda item: parser.parse(item['Name']), items)
        results = []
        [results.append(x) for x in items if x not in results]
        return results

    def __parseRows(self, notice: EnchantmentProbabilityNotice) -> List[EnchantmentRange]:
        parser = RowParser()
        items = filter(lambda item: not self.__isCategory(item), notice['Items'])
        items = map(lambda item: parser.parse(item['Name']), items)
        results = []
        [results.append(x) for x in items if x not in results]
        return results

    def __parseSerial(self, notice: EnchantmentProbabilityNotice) -> EnchantmentSerial:
        return {
            'Name': notice['Name'],
            'Des': notice['Des'],
            'Url': notice['Url'],
            'API': notice['API']
        }

    def __parseProbability(self, itemValue):
        return float(itemValue.replace('%', '')) / 100

    def __isCategory(self, item: EnchantmentProbabilityNoticeItem):
        return not ('欄' in set(item['Name']))