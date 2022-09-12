from typing import List
from core import EnchantmentProbabilityNotice, EnchantmentProbabilityNoticeItem, EnchantmentCategory, EnchantmentSerial, EnchantmentRange, EnchantmentRow, EnchantableAttributeProbability
from enchantment_attribute_parser import EnchantmentAttributeParser

class EnchantmentProbabilityNoticeConverter:
    notice: EnchantmentProbabilityNotice

    def __init__(self, notice: EnchantmentProbabilityNotice):
        self.notice = notice

    def convert(self):
        self.serial = self.__toSerial()
        self.categories = self.__toCategories()
        self.ranges = self.__toRanges()
        self.rows = self.__toRows()
        self.attributeProbabilities = self.__toAttributeProbabilities()

    def __toSerial(self) -> EnchantmentSerial:
        return {
            'Name': self.notice['Name'],
            'Des': self.notice['Des'],
            'Url': self.notice['Url'],
            'API': self.notice['API']
        }

    def __toCategories(self) -> List[EnchantmentCategory]:
        parser = EnchantmentAttributeParser()
        items = filter(lambda x: not self.__checkEnchantmentRow(x), self.notice['Items'])
        items = map(lambda x: parser.parse(x['Name'])['Category'], items)
        results = []
        [results.append(x) for x in items if x not in results]
        return results

    def __toRanges(self) -> List[EnchantmentRange]:
        parser = EnchantmentAttributeParser()
        items = filter(lambda x: not self.__checkEnchantmentRow(x), self.notice['Items'])
        items = map(lambda x: parser.parse(x['Name'])['Range'], items)
        results = []
        [results.append(x) for x in items if x not in results]
        return results

    def __toRows(self) -> List[EnchantmentRow]:
        indexList = [i for i,v in enumerate(self.notice['Items']) if self.__checkEnchantmentRow(v)]
        results = []
        for index in indexList:
            row: EnchantmentRow = self.__parseEnchantmentRow(self.notice['Items'][index]['Name'])
            results.append(row)
        return results

    def __toAttributeProbabilities(self) -> List[EnchantableAttributeProbability]:
        parser = EnchantmentAttributeParser()
        indexList = [i for i,v in enumerate(self.notice['Items']) if self.__checkEnchantmentRow(v)]
        indexList.append(len(self.notice['Items']))
        results = []
        for i in range(len(indexList) - 1):
            rowItemName = self.notice['Items'][indexList[i]]['Name']
            items = self.notice['Items'][indexList[i] + 1:indexList[i + 1]]
            results += map(lambda x: {
                'Attribute': parser.parse(x['Name']),
                'Probability': self.__parseProbibility(x['Value']),
                'Row': self.__parseEnchantmentRow(rowItemName),
                'Serial': self.serial,
            }, items)
        return results


    def __checkEnchantmentRow(self, item: EnchantmentProbabilityNoticeItem):
        s = set(item['Name'])
        return '第' in s and '欄' in s

    def __parseEnchantmentRow(self, itemName: str) -> EnchantmentRow:
        rowNumber = 0
        if itemName.find('第一欄') != -1:
            rowNumber = 1
        elif itemName.find('第二欄') != -1:
            rowNumber = 2
        elif itemName.find('第三欄') != -1:
            rowNumber = 3
        elif itemName.find('第四欄') != -1:
            rowNumber = 4

        probability = ''
        for ch in itemName:
            if ch.isdigit():
                probability += ch
        if len(probability) == 0:
            probability = 1
        else:
            probability = int(probability) / 100
        return {
            'Probability': probability,
            'RowNumber': rowNumber,
        }

    def __parseProbibility(self, prob: str) -> float:
        return float(prob.replace('%', '')) / 100