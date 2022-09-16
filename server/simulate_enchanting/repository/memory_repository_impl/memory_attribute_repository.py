from unicodedata import category
from simulate_enchanting.core.core import EnchantableAttribute
from simulate_enchanting.repository.memory_repository import MemoryRepository
from simulate_enchanting.repository.unit_of_work import UnitOfWork

class MemoryAttributeRepository(MemoryRepository):
    def __init__(self, unitOfWork: UnitOfWork):
        self.__unitOfWork = unitOfWork

    def add(self, __object: EnchantableAttribute):
        super().add(self.__toSavedObject(__object))

    def getById(self, __id: int):
        return self.__fromSavedObject(super().getById(__id))

    def getId(self, __object) -> int:
        return super().getId(self.__toSavedObject(__object))

    def getAll(self):
        results = super().getAll()
        return list(map(lambda p: self.__fromSavedObject(p), results))

    def getBySerialId(self, __serialId):
        results = list(filter(lambda i: i['SerialId'] == __serialId, self.__db))
        return list(map(lambda p: self.__fromSavedObject(p), results))

    @property
    def _props(self):
        return ['Probability', 'CategoryId', 'RangeId', 'RowId', 'SerialId']

    def __toSavedObject(self, __object: EnchantableAttribute): 
        __savedObject = { 'Probability': __object['Probability'] }
        __savedObject['CategoryId'] = self.__unitOfWork.categoryRepository.getId(__object['Category'])
        __savedObject['RangeId'] = self.__unitOfWork.rangeRepository.getId(__object['Range'])
        __savedObject['RowId'] = self.__unitOfWork.rowRepository.getId(__object['Row'])
        __savedObject['SerialId'] = self.__unitOfWork.serialRepository.getId(__object['Serial'])
        return __savedObject

    def __fromSavedObject(self, __savedObject) -> EnchantableAttribute:
        __object = { 'Id': __savedObject['Id'], 'Probability': __savedObject['Probability'] }
        __object['Category'] = self.__unitOfWork.categoryRepository.getById(__savedObject['CategoryId'])
        __object['Range'] = self.__unitOfWork.rangeRepository.getById(__savedObject['RangeId'])
        __object['Row'] = self.__unitOfWork.rowRepository.getById(__savedObject['RowId'])
        __object['Serial'] = self.__unitOfWork.serialRepository.getById(__savedObject['SerialId'])
        return __object