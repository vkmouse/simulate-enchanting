from unicodedata import category
import unittest
from simulate_enchanting.repository import UnitOfWork, MemoryUnitOfWork, MySQLUnitOfWork


class TestAttributeRepository(unittest.TestCase):
    def preprocess(self, unitOfWork: UnitOfWork):
        unitOfWork.categoryRepository.add({ 'Name': 'Test1', 'IsPercentage': True })
        unitOfWork.categoryRepository.add({ 'Name': 'Test2', 'IsPercentage': True })
        unitOfWork.categoryRepository.add({ 'Name': 'Test3', 'IsPercentage': True })

        unitOfWork.rangeRepository.add({ 'Start': 1, 'Stop': 2, 'Step': 1 })
        unitOfWork.rangeRepository.add({ 'Start': 2, 'Stop': 4, 'Step': 1 })
        unitOfWork.rangeRepository.add({ 'Start': 3, 'Stop': 6, 'Step': 3 })

        unitOfWork.rowRepository.add({ 'Probability': 0.05, 'RowNumber': 2 })
        unitOfWork.rowRepository.add({ 'Probability': 1, 'RowNumber': 1 })
        unitOfWork.rowRepository.add({ 'Probability': 0.5, 'RowNumber': 3 })

        unitOfWork.serialRepository.add({ 'Name': 'Test1', 'Des': 'Des1', 'Url': 'Url1', 'API': 'API1' })
        unitOfWork.serialRepository.add({ 'Name': 'Test2', 'Des': 'Des2', 'Url': 'Url2', 'API': 'API2' })
        unitOfWork.serialRepository.add({ 'Name': 'Test3', 'Des': 'Des3', 'Url': 'Url3', 'API': 'API3' })

    def addTesting(self, unitOfWork: UnitOfWork):
        self.preprocess(unitOfWork)
        attribute = { 
            'Id': 1,
            'Probability': 0.035, 
            'Category': unitOfWork.categoryRepository.getById(1),
            'Range': unitOfWork.rangeRepository.getById(1),
            'Row': unitOfWork.rowRepository.getById(1),
            'Serial': unitOfWork.serialRepository.getById(1),
        }
        unitOfWork.attributeRepository.add(attribute)
        self.assertEqual(unitOfWork.attributeRepository.getById(1), attribute)

    def getByIdTesting(self, unitOfWork: UnitOfWork):
        self.preprocess(unitOfWork)
        for i in range(1, 4):
            unitOfWork.attributeRepository.add({             
                'Probability': i, 
                'Category': unitOfWork.categoryRepository.getById(i),
                'Range': unitOfWork.rangeRepository.getById(i),
                'Row': unitOfWork.rowRepository.getById(i),
                'Serial': unitOfWork.serialRepository.getById(i)
            })
        actual = unitOfWork.attributeRepository.getById(3)
        self.assertEqual(actual, {
            'Id': 3,
            'Probability': 3, 
            'Category': unitOfWork.categoryRepository.getById(3),
            'Range': unitOfWork.rangeRepository.getById(3),
            'Row': unitOfWork.rowRepository.getById(3),
            'Serial': unitOfWork.serialRepository.getById(3)
        })
        
    def getIdTesting(self, unitOfWork: UnitOfWork):
        self.preprocess(unitOfWork)
        for i in range(1, 4):
            unitOfWork.attributeRepository.add({             
                'Probability': i, 
                'Category': unitOfWork.categoryRepository.getById(i),
                'Range': unitOfWork.rangeRepository.getById(i),
                'Row': unitOfWork.rowRepository.getById(i),
                'Serial': unitOfWork.serialRepository.getById(i)
            })
        actual = unitOfWork.attributeRepository.getId({ 
            'Probability': 3, 
            'Category': unitOfWork.categoryRepository.getById(3),
            'Range': unitOfWork.rangeRepository.getById(3),
            'Row': unitOfWork.rowRepository.getById(3),
            'Serial': unitOfWork.serialRepository.getById(3),
        })
        self.assertEqual(actual, 3)

    def getByIdExceptionTesting(self, unitOfWork: UnitOfWork):
        self.preprocess(unitOfWork)
        for i in range(1, 4):
            unitOfWork.attributeRepository.add({             
                'Probability': i, 
                'Category': unitOfWork.categoryRepository.getById(i),
                'Range': unitOfWork.rangeRepository.getById(i),
                'Row': unitOfWork.rowRepository.getById(i),
                'Serial': unitOfWork.serialRepository.getById(i)
            })
        unitOfWork.attributeRepository.getById(1)
        try:
            unitOfWork.attributeRepository.getById(4)
        except Exception:
            return
        self.fail()

    def getIdExceptionTesting(self, unitOfWork: UnitOfWork):
        self.preprocess(unitOfWork)
        for i in range(1, 4):
            unitOfWork.attributeRepository.add({             
                'Probability': i, 
                'Category': unitOfWork.categoryRepository.getById(i),
                'Range': unitOfWork.rangeRepository.getById(i),
                'Row': unitOfWork.rowRepository.getById(i),
                'Serial': unitOfWork.serialRepository.getById(i)
            })
        try:
            unitOfWork.attributeRepository.getId({ 
                'Probability': 3, 
                'Category': unitOfWork.categoryRepository.getById(2),
                'Range': unitOfWork.rangeRepository.getById(3),
                'Row': unitOfWork.rowRepository.getById(3),
                'Serial': unitOfWork.serialRepository.getById(3),
            })
        except Exception:
            return
        self.fail()

    def createMemoryUnitOfWork(self):
        unitOfWork = MemoryUnitOfWork()
        unitOfWork.initialize()
        return unitOfWork

    def testMemoryAdd(self):
        unitOfWork = self.createMemoryUnitOfWork()
        self.addTesting(unitOfWork)

    def testMemoryGetById(self):
        unitOfWork = self.createMemoryUnitOfWork()
        self.getByIdTesting(unitOfWork)

    def testMemoryGetId(self):
        unitOfWork = self.createMemoryUnitOfWork()
        self.getIdTesting(unitOfWork)

    def testMemoryGetByIdException(self):
        unitOfWork = self.createMemoryUnitOfWork()
        self.getByIdExceptionTesting(unitOfWork)

    def testMemoryGetIdException(self):
        unitOfWork = self.createMemoryUnitOfWork()
        self.getIdExceptionTesting(unitOfWork)

    def createMySQLUnitOfWork(self):
        unitOfWork = MySQLUnitOfWork(testMode=True)
        unitOfWork.initialize()
        return unitOfWork

    def testMySQLAdd(self):
        unitOfWork = self.createMemoryUnitOfWork()
        # self.addTesting(unitOfWork)

if __name__ == '__main__':
    unittest.main()