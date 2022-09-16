import unittest
from simulate_enchanting.repository import MemoryRowRepository, MySQLRowRepository, MySQLWorker

class TestRowRepository(unittest.TestCase):
    def addTesting(self, repository):
        repository.add({ 'Probability': 0.05, 'RowNumber': 2 })
        actual = repository.getById(1)
        self.assertEqual(actual, { 'Id': 1, 'Probability': 0.05, 'RowNumber': 2 })

    def getByIdTesting(self, repository):
        repository.add({ 'Probability': 0.05, 'RowNumber': 2 })
        repository.add({ 'Probability': 1, 'RowNumber': 1 })
        repository.add({ 'Probability': 0.5, 'RowNumber': 3 })
        actual = repository.getById(3)
        self.assertEqual(actual, { 'Id': 3, 'Probability': 0.5, 'RowNumber': 3 })

    def getIdTesting(self, repository):
        repository.add({ 'Probability': 0.05, 'RowNumber': 2 })
        repository.add({ 'Probability': 1, 'RowNumber': 1 })
        repository.add({ 'Probability': 0.05, 'RowNumber': 3 })
        actual = repository.getId({ 'Probability': 0.05, 'RowNumber': 3 })
        self.assertEqual(actual, 3)

    def getByIdExceptionTesting(self, repository):
        repository.add({ 'Probability': 0.05, 'RowNumber': 3 })
        repository.add({ 'Probability': 0.05, 'RowNumber': 3 })
        repository.getById(1)
        try:
            repository.getById(2)
        except Exception:
            return
        self.fail()

    def getIdExceptionTesting(self, repository):
        repository.add({ 'Probability': 0.05, 'RowNumber': 3 })
        repository.getId({ 'Probability': 0.05, 'RowNumber': 3 })
        try:
            repository.getId({ 'Probability': 0.049, 'RowNumber': 3 })
        except Exception:
            return
        self.fail()

    def getAllTesting(self, repository):
        repository.add({ 'Probability': 0.05, 'RowNumber': 2 })
        repository.add({ 'Probability': 1, 'RowNumber': 1 })
        repository.add({ 'Probability': 0.05, 'RowNumber': 3 })
        actual = repository.getAll()
        self.assertEqual(len(actual), 3)

    def createMemoryRepository(self):
        repository = MemoryRowRepository()
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
        repository = MySQLRowRepository(worker, testMode=True)
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
    def testMemoryGetAll(self):
        repository = self.createMySQLRepository()
        self.getAllTesting(repository)

if __name__ == '__main__':
    unittest.main()