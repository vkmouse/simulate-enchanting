import unittest
from simulate_enchanting.repository import MemoryCategoryRepository, MySQLCategoryRepository, MySQLWorker

class TestCategoryRepository(unittest.TestCase):
    def addTesting(self, repository):
        repository.add({ 'Name': 'Test1', 'IsPercentage': True })
        actual = repository.getById(1)
        self.assertEqual(actual, { 'Id': 1, 'Name': 'Test1', 'IsPercentage': True })

    def getByIdTesting(self, repository):
        repository.add({ 'Name': 'Test1', 'IsPercentage': True })
        repository.add({ 'Name': 'Test2', 'IsPercentage': True })
        repository.add({ 'Name': 'Test3', 'IsPercentage': True })
        actual = repository.getById(3)
        self.assertEqual(actual, { 'Id': 3, 'Name': 'Test3', 'IsPercentage': True })

    def getIdTesting(self, repository):
        repository.add({ 'Name': 'Test1', 'IsPercentage': True })
        repository.add({ 'Name': 'Test2', 'IsPercentage': True })
        repository.add({ 'Name': 'Test3', 'IsPercentage': True })
        actual = repository.getId({ 'Name': 'Test3', 'IsPercentage': True })
        self.assertEqual(actual, 3)

    def getByIdExceptionTesting(self, repository):
        repository.add({ 'Name': 'Test1', 'IsPercentage': True })
        repository.add({ 'Name': 'Test1', 'IsPercentage': True })
        repository.getById(1)
        try:
            repository.getById(2)
        except Exception:
            return
        self.fail()

    def getIdExceptionTesting(self, repository):
        repository.add({ 'Name': 'Test1', 'IsPercentage': True })
        repository.getId({ 'Name': 'Test1', 'IsPercentage': True })
        try:
            repository.getId({ 'Name': 'Test1', 'IsPercentage': False })
        except Exception:
            return
        self.fail()

    def getAllTesting(self, repository):
        repository.add({ 'Name': 'Test1', 'IsPercentage': True })
        repository.add({ 'Name': 'Test2', 'IsPercentage': True })
        repository.add({ 'Name': 'Test3', 'IsPercentage': True })
        actual = repository.getAll()
        self.assertEqual(len(actual), 3)

    def createMemoryRepository(self):
        repository = MemoryCategoryRepository()
        repository.initialize()
        return repository

    def testMemoryAdd(self):
        repository = self.createMemoryRepository()
        self.addTesting(repository)

    def testMemoryGetById(self):
        repository = self.createMemoryRepository()
        self.getByIdTesting(repository)

    def testMemoryGetId(self):
        repository = self.createMemoryRepository()
        self.getIdTesting(repository)

    def testMemoryGetByIdException(self):
        repository = self.createMemoryRepository()
        self.getByIdExceptionTesting(repository)

    def testMemoryGetIdException(self):
        repository = self.createMemoryRepository()
        self.getIdExceptionTesting(repository)

    def testMemoryGetAll(self):
        repository = self.createMemoryRepository()
        self.getAllTesting(repository)

    def createMySQLRepository(self):
        worker = MySQLWorker()
        worker.connect()
        repository = MySQLCategoryRepository(worker, testMode=True)
        repository.initialize()
        return repository

    @unittest.skipIf(not MySQLWorker.isAvailable(), 'MySQL is not available')
    def testMySQLAdd(self):
        repository = self.createMySQLRepository()
        self.addTesting(repository)

    @unittest.skipIf(not MySQLWorker.isAvailable(), 'MySQL is not available')
    def testMySQLGetById(self):
        repository = self.createMySQLRepository()
        self.getByIdTesting(repository)

    @unittest.skipIf(not MySQLWorker.isAvailable(), 'MySQL is not available')
    def testMySQLGetId(self):
        repository = self.createMySQLRepository()
        self.getIdTesting(repository)

    @unittest.skipIf(not MySQLWorker.isAvailable(), 'MySQL is not available')
    def testMySQLGetByIdException(self):
        repository = self.createMySQLRepository()
        self.getByIdExceptionTesting(repository)

    @unittest.skipIf(not MySQLWorker.isAvailable(), 'MySQL is not available')
    def testMySQLGetIdException(self):
        repository = self.createMySQLRepository()
        self.getIdExceptionTesting(repository)

    @unittest.skipIf(not MySQLWorker.isAvailable(), 'MySQL is not available')
    def testMySQLGetAll(self):
        repository = self.createMySQLRepository()
        self.getAllTesting(repository)

if __name__ == '__main__':
    unittest.main()