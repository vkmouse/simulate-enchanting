from typing import List
from simulate_enchanting.repository.repository import Repository

class MemoryRepository(Repository):
    def initialize(self):
        self.__db = []

    def add(self, __object):
        results = list(filter(lambda i: self.__compare(i, __object), self.__db))
        if len(results) == 0:
            __object['Id'] = len(self.__db) + 1
            self.__db.append(__object)
    
    def getById(self, __id: int):
        results = list(filter(lambda i: i['Id'] == __id, self.__db))
        if len(results) == 0:
            raise Exception('[MemoryRepository] object is not existed')
        return results[0]

    def getId(self, __object) -> int:
        results = list(filter(lambda i: self.__compare(i, __object), self.__db))
        if len(results) == 0:
            raise Exception('[MemoryRepository] object is not existed')
        return results[0]['Id']
    
    def __compare(self, lhs, rhs) -> bool:
        for prop in self._props:
            if lhs[prop] != rhs[prop]:
                return False
        return True

    @property
    def _props(self) -> List[str]: 
        pass
