import abc
from simulate_enchanting.repository.repository import Repository

class UnitOfWork(metaclass=abc.ABCMeta):
    def initialize(self):
        self.__attributeRepository = self._createAttributeRepository()
        self.__categoryRepository = self._createCategoryRepository()
        self.__rangeRepository = self._createRangeRepository()
        self.__rowRepository = self._createRowRepository()
        self.__serialRepository = self._createSerialRepository()

    @property
    def attributeRepository(self) -> Repository:
        return self.__attributeRepository

    @property
    def categoryRepository(self) -> Repository:
        return self.__categoryRepository
    
    @property
    def rangeRepository(self) -> Repository:
        return self.__rangeRepository

    @property
    def rowRepository(self) -> Repository:
        return self.__rowRepository

    @property
    def serialRepository(self) -> Repository:
        return self.__serialRepository

    def _createAttributeRepository(self) -> Repository:
        return NotImplemented

    def _createCategoryRepository(self) -> Repository:
        return NotImplemented

    def _createRangeRepository(self) -> Repository:
        return NotImplemented

    def _createRowRepository(self) -> Repository:
        return NotImplemented

    def _createSerialRepository(self) -> Repository:
        return NotImplemented
