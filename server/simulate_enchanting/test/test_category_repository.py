import unittest
from simulate_enchanting.repository import MemoryCategoryRepository, MySQLCategoryRepository, MySQLWorker

class TestCategoryRepository(unittest.TestCase):
    def addTesting(self, repository):
        repository.add({ 'Name': 'Test1', 'IsPercentage': True })
        actual = repository.getById(1)
        self.assertEqual(actual, { 'Id': 1, 'Name': 'Test1', 'IsPercentage': True })
        repository = None

    def getByIdTesting(self, repository):
        repository.add({ 'Name': 'Test1', 'IsPercentage': True })
        repository.add({ 'Name': 'Test2', 'IsPercentage': True })
        repository.add({ 'Name': 'Test3', 'IsPercentage': True })
        actual = repository.getById(3)
        self.assertEqual(actual, { 'Id': 3, 'Name': 'Test3', 'IsPercentage': True })
        repository = None

    def getIdTesting(self, repository):
        repository.add({ 'Name': 'Test1', 'IsPercentage': True })
        repository.add({ 'Name': 'Test2', 'IsPercentage': True })
        repository.add({ 'Name': 'Test3', 'IsPercentage': True })
        actual = repository.getId({ 'Name': 'Test3', 'IsPercentage': True })
        self.assertEqual(actual, 3)
        repository = None

    def getByIdExceptionTesting(self, repository):
        try:
            repository.getById(0)
            self.fail()
        except Exception:
            pass
        repository = None

    def getIdExceptionTesting(self, repository):
        try:
            repository.getId({ 'Name': 'Test1', 'IsPercentage': True })
            self.fail()
        except Exception:
            pass
        repository = None

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

if __name__ == '__main__':
    unittest.main()