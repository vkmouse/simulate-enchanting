import unittest
from simulate_enchanting.repository import MemoryRangeRepository

class TestRangeRepository(unittest.TestCase):
    def addTesting(self, repository):
        repository.add({ 'Start': 1, 'Stop': 2, 'Step': 1 })
        actual = repository.getById(1)
        self.assertEqual(actual, { 'Id': 1, 'Start': 1, 'Stop': 2, 'Step': 1 })
        repository = None

    def getByIdTesting(self, repository):
        repository.add({ 'Start': 1, 'Stop': 2, 'Step': 1 })
        repository.add({ 'Start': 2, 'Stop': 4, 'Step': 1 })
        repository.add({ 'Start': 3, 'Stop': 6, 'Step': 3 })
        actual = repository.getById(3)
        self.assertEqual(actual, { 'Id': 3, 'Start': 3, 'Stop': 6, 'Step': 3 })
        repository = None

    def getIdTesting(self, repository):
        repository.add({ 'Start': 1, 'Stop': 2, 'Step': 1 })
        repository.add({ 'Start': 2, 'Stop': 4, 'Step': 1 })
        repository.add({ 'Start': 3, 'Stop': 6, 'Step': 3 })
        actual = repository.getId({ 'Start': 3, 'Stop': 6, 'Step': 3 })
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
            repository.getId({ 'Start': 3, 'Stop': 6, 'Step': 3 })
            self.fail()
        except Exception:
            pass
        repository = None

    def createMemoryRepository(self):
        return MemoryRangeRepository()

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