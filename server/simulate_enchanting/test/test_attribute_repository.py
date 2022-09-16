import unittest
from simulate_enchanting.repository import UnitOfWork, MemoryUnitOfWork, MySQLUnitOfWork, MySQLWorker

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
        unitOfWork.attributeRepository.add({ 
            'Probability': 0.035, 
            'Category': unitOfWork.categoryRepository.getById(1),
            'Range': unitOfWork.rangeRepository.getById(1),
            'Row': unitOfWork.rowRepository.getById(1),
            'Serial': unitOfWork.serialRepository.getById(1),
        })
        self.assertEqual(unitOfWork.attributeRepository.getById(1), { 
            'Id': 1,
            'Probability': 0.035, 
            'Category': unitOfWork.categoryRepository.getById(1),
            'Range': unitOfWork.rangeRepository.getById(1),
            'Row': unitOfWork.rowRepository.getById(1),
            'Serial': unitOfWork.serialRepository.getById(1),
        })

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
        for i in range(2):
            for j in range(1, 4):
                unitOfWork.attributeRepository.add({             
                    'Probability': j, 
                    'Category': unitOfWork.categoryRepository.getById(j),
                    'Range': unitOfWork.rangeRepository.getById(j),
                    'Row': unitOfWork.rowRepository.getById(j),
                    'Serial': unitOfWork.serialRepository.getById(j)
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

    def getAllTesting(self, unitOfWork: UnitOfWork):
        self.preprocess(unitOfWork)
        for i in range(1, 4):
            unitOfWork.attributeRepository.add({             
                'Probability': i, 
                'Category': unitOfWork.categoryRepository.getById(i),
                'Range': unitOfWork.rangeRepository.getById(i),
                'Row': unitOfWork.rowRepository.getById(i),
                'Serial': unitOfWork.serialRepository.getById(i)
            })
        actual = unitOfWork.attributeRepository.getAll()
        self.assertEqual(len(actual), 3)
        self.assertEqual(actual[0], {
            'Id': 1,
            'Probability': 1,
            'Category': { 'Id': 1, 'Name': 'Test1', 'IsPercentage': True },
            'Range': { 'Id': 1, 'Start': 1, 'Stop': 2, 'Step': 1 },
            'Row': { 'Id': 1, 'Probability': 0.05, 'RowNumber': 2 },
            'Serial': { 'Id': 1, 'Name': 'Test1', 'Des': 'Des1', 'Url': 'Url1', 'API': 'API1' },
        })
        self.assertEqual(actual[1], {
            'Id': 2,
            'Probability': 2,
            'Category': { 'Id': 2, 'Name': 'Test2', 'IsPercentage': True },
            'Range': { 'Id': 2, 'Start': 2, 'Stop': 4, 'Step': 1 },
            'Row': { 'Id': 2, 'Probability': 1, 'RowNumber': 1 },
            'Serial': { 'Id': 2, 'Name': 'Test2', 'Des': 'Des2', 'Url': 'Url2', 'API': 'API2' },
        })
        self.assertEqual(actual[2], {
            'Id': 3,
            'Probability': 3,
            'Category': { 'Id': 3, 'Name': 'Test3', 'IsPercentage': True },
            'Range': { 'Id': 3, 'Start': 3, 'Stop': 6, 'Step': 3 },
            'Row': { 'Id': 3, 'Probability': 0.5, 'RowNumber': 3 },
            'Serial': { 'Id': 3, 'Name': 'Test3', 'Des': 'Des3', 'Url': 'Url3', 'API': 'API3' },
        })

    def getBySerialIdTesting(self, unitOfWork: UnitOfWork):
        self.preprocess(unitOfWork)
        unitOfWork.attributeRepository.add({ 
            'Probability': 0.035, 
            'Category': unitOfWork.categoryRepository.getById(1),
            'Range': unitOfWork.rangeRepository.getById(1),
            'Row': unitOfWork.rowRepository.getById(1),
            'Serial': unitOfWork.serialRepository.getById(1),
        })
        unitOfWork.attributeRepository.add({ 
            'Probability': 0.06, 
            'Category': unitOfWork.categoryRepository.getById(2),
            'Range': unitOfWork.rangeRepository.getById(2),
            'Row': unitOfWork.rowRepository.getById(2),
            'Serial': unitOfWork.serialRepository.getById(2),
        })
        unitOfWork.attributeRepository.add({ 
            'Probability': 0.07, 
            'Category': unitOfWork.categoryRepository.getById(3),
            'Range': unitOfWork.rangeRepository.getById(3),
            'Row': unitOfWork.rowRepository.getById(3),
            'Serial': unitOfWork.serialRepository.getById(1),
        })
        actual = unitOfWork.attributeRepository.getBySerialId(1)
        self.assertEqual(len(actual), 2)
        self.assertEqual(actual[0], {
            'Id': 1,
            'Probability': 0.035,
            'Category': { 'Id': 1, 'Name': 'Test1', 'IsPercentage': True },
            'Range': { 'Id': 1, 'Start': 1, 'Stop': 2, 'Step': 1 },
            'Row': { 'Id': 1, 'Probability': 0.05, 'RowNumber': 2 },
            'Serial': { 'Id': 1, 'Name': 'Test1', 'Des': 'Des1', 'Url': 'Url1', 'API': 'API1' },
        })
        self.assertEqual(actual[1], {
            'Id': 3,
            'Probability': 0.07,
            'Category': { 'Id': 3, 'Name': 'Test3', 'IsPercentage': True },
            'Range': { 'Id': 3, 'Start': 3, 'Stop': 6, 'Step': 3 },
            'Row': { 'Id': 3, 'Probability': 0.5, 'RowNumber': 3 },
            'Serial': { 'Id': 1, 'Name': 'Test1', 'Des': 'Des1', 'Url': 'Url1', 'API': 'API1' },
        })

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

    def testMemoryGetAll(self):
        repository = self.createMemoryUnitOfWork()
        self.getAllTesting(repository)

    def testMemoryGetBySerialId(self):
        repository = self.createMemoryUnitOfWork()
        self.getBySerialIdTesting(repository)

    def createMySQLUnitOfWork(self):
        unitOfWork = MySQLUnitOfWork(testMode=True)
        unitOfWork.initialize()
        return unitOfWork

    @unittest.skipIf(not MySQLWorker.isAvailable(), 'MySQL is not available')
    def testMySQLAdd(self):
        unitOfWork = self.createMySQLUnitOfWork()
        self.addTesting(unitOfWork)

    @unittest.skipIf(not MySQLWorker.isAvailable(), 'MySQL is not available')
    def testMySQLGetById(self):
        unitOfWork = self.createMySQLUnitOfWork()
        self.getByIdTesting(unitOfWork)

    @unittest.skipIf(not MySQLWorker.isAvailable(), 'MySQL is not available')
    def testMemoryGetId(self):
        unitOfWork = self.createMySQLUnitOfWork()
        self.getIdTesting(unitOfWork)

    @unittest.skipIf(not MySQLWorker.isAvailable(), 'MySQL is not available')
    def testMySQLGetByIdException(self):
        unitOfWork = self.createMySQLUnitOfWork()
        self.getByIdExceptionTesting(unitOfWork)

    @unittest.skipIf(not MySQLWorker.isAvailable(), 'MySQL is not available')
    def testMemoryGetIdException(self):
        unitOfWork = self.createMySQLUnitOfWork()
        self.getIdExceptionTesting(unitOfWork)

    @unittest.skipIf(not MySQLWorker.isAvailable(), 'MySQL is not available')
    def testMySQLGetAll(self):
        unitOfWork = self.createMySQLUnitOfWork()
        self.getAllTesting(unitOfWork)

    @unittest.skipIf(not MySQLWorker.isAvailable(), 'MySQL is not available')
    def testMySQLGetBySerialId(self):
        unitOfWork = self.createMySQLUnitOfWork()
        self.getBySerialIdTesting(unitOfWork)

if __name__ == '__main__':
    unittest.main()