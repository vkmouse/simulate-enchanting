import unittest
from simulate_enchanting.repository import MemoryRowRepository

class TestRowRepository(unittest.TestCase):
    def addTesting(self, repository):
        repository.add({ 'Probability': 0.05, 'RowNumber': 2 })
        actual = repository.getById(1)
        self.assertEqual(actual, { 'Id': 1, 'Probability': 0.05, 'RowNumber': 2 })
        repository = None

    def getByIdTesting(self, repository):
        repository.add({ 'Probability': 0.05, 'RowNumber': 2 })
        repository.add({ 'Probability': 1, 'RowNumber': 1 })
        repository.add({ 'Probability': 0.5, 'RowNumber': 3 })
        actual = repository.getById(3)
        self.assertEqual(actual, { 'Id': 3, 'Probability': 0.5, 'RowNumber': 3 })
        repository = None

    def getIdTesting(self, repository):
        repository.add({ 'Probability': 0.05, 'RowNumber': 2 })
        repository.add({ 'Probability': 1, 'RowNumber': 1 })
        repository.add({ 'Probability': 0.5, 'RowNumber': 3 })
        actual = repository.getId({ 'Probability': 0.5, 'RowNumber': 3 })
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
            repository.getId({ 'Probability': 0.5, 'RowNumber': 3 })
            self.fail()
        except Exception:
            pass
        repository = None

    def createMemoryRepository(self):
        return MemoryRowRepository()

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

if __name__ == '__main__':
    unittest.main()