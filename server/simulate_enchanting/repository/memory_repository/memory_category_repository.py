from simulate_enchanting.core import EnchantmentCategory
from simulate_enchanting.repository.repository import Repository

class MemoryCategoryRepository(Repository):
    def __init__(self):
        self.__db: list[EnchantmentCategory] = []

    def add(self, __object: EnchantmentCategory):
        __object['Id'] = len(self.__db) + 1
        self.__db.append(__object)
    
    def getById(self, __id: int) -> EnchantmentCategory:
        results = list(filter(lambda i: i['Id'] == __id, self.__db))
        if len(results) == 0:
            raise Exception('[MemoryCategoryRepository] object is not existed')
        return results[0]

    def getId(self, __object: EnchantmentCategory) -> int:
        results = list(filter(lambda i: self.__compare(i, __object), self.__db))
        if len(results) == 0:
            raise Exception('[MemoryCategoryRepository] object is not existed')
        return results[0]['Id']
    
    def __compare(self, lhs, rhs) -> bool:
        return lhs['IsPercentage'] == rhs['IsPercentage'] and lhs['Name'] == rhs['Name']