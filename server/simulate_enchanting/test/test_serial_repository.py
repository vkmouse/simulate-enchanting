import unittest
from simulate_enchanting.repository import MemorySerialRepository, MySQLSerialRepository, MySQLWorker

class TestSerialRepository(unittest.TestCase):
    def addTesting(self, repository):
        repository.add({ 'Name': 'Test1', 'Des': 'Des1', 'Url': 'Url1', 'API': 'API1' })
        actual = repository.getById(1)
        self.assertEqual(actual, { 'Id': 1, 'Name': 'Test1', 'Des': 'Des1', 'Url': 'Url1', 'API': 'API1' })

    def getByIdTesting(self, repository):
        repository.add({ 'Name': 'Test1', 'Des': 'Des1', 'Url': 'Url1', 'API': 'API1' })
        repository.add({ 'Name': 'Test2', 'Des': 'Des2', 'Url': 'Url2', 'API': 'API2' })
        repository.add({ 'Name': 'Test3', 'Des': 'Des3', 'Url': 'Url3', 'API': 'API3' })
        actual = repository.getById(3)
        self.assertEqual(actual, { 'Id': 3, 'Name': 'Test3', 'Des': 'Des3', 'Url': 'Url3', 'API': 'API3' })

    def getIdTesting(self, repository):
        repository.add({ 'Name': 'Test1', 'Des': 'Des1', 'Url': 'Url1', 'API': 'API1' })
        repository.add({ 'Name': 'Test2', 'Des': 'Des2', 'Url': 'Url2', 'API': 'API2' })
        repository.add({ 'Name': 'Test3', 'Des': 'Des3', 'Url': 'Url3', 'API': 'API3' })
        actual = repository.getId({ 'Name': 'Test3', 'Des': 'Des3', 'Url': 'Url3', 'API': 'API3' })
        self.assertEqual(actual, 3)

    def getByIdExceptionTesting(self, repository):
        repository.add({ 'Name': 'Test1', 'Des': 'Des1', 'Url': 'Url1', 'API': 'API1' })
        repository.add({ 'Name': 'Test1', 'Des': 'Des1', 'Url': 'Url1', 'API': 'API1' })
        repository.getById(1)
        try:
            repository.getById(2)
        except Exception:
            return
        self.fail()

    def getIdExceptionTesting(self, repository):
        repository.add({ 'Name': 'Test1', 'Des': 'Des1', 'Url': 'Url1', 'API': 'API1' })
        repository.getId({ 'Name': 'Test1', 'Des': 'Des1', 'Url': 'Url1', 'API': 'API1' })
        try:
            repository.getId({ 'Name': '', 'Des': '', 'Url': '', 'API': '' })
        except Exception:
            return
        self.fail()
        
    def getAllTesting(self, repository):
        repository.add({ 'Name': 'Test1', 'Des': 'Des1', 'Url': 'Url1', 'API': 'API1' })
        repository.add({ 'Name': 'Test2', 'Des': 'Des2', 'Url': 'Url2', 'API': 'API2' })
        repository.add({ 'Name': 'Test3', 'Des': 'Des3', 'Url': 'Url3', 'API': 'API3' })
        actual = repository.getAll()
        self.assertEqual(len(actual), 3)
        self.assertEqual(actual[0], { 'Id': 1, 'Name': 'Test1', 'Des': 'Des1', 'Url': 'Url1', 'API': 'API1' })
        self.assertEqual(actual[1], { 'Id': 2, 'Name': 'Test2', 'Des': 'Des2', 'Url': 'Url2', 'API': 'API2' })
        self.assertEqual(actual[2], { 'Id': 3, 'Name': 'Test3', 'Des': 'Des3', 'Url': 'Url3', 'API': 'API3' })

    def createMemoryRepository(self):
        repository = MemorySerialRepository()
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
        repository = MySQLSerialRepository(worker, testMode=True)
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