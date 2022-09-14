from functools import cache
import unittest
from simulate_enchanting.repository import MemoryCategoryRepository, MySQLCategoryRepository

class TestCategoryRepository(unittest.TestCase):
    def createRepository(self):
        return MemoryCategoryRepository()

    def testAdd(self):
        repository = self.createRepository()
        repository.add({ 'Name': 'Test1', 'IsPercentage': True })
        actual = repository.getById(1)
        self.assertEqual(actual, { 'Id': 1, 'Name': 'Test1', 'IsPercentage': True })
        repository = None

    def testGetById(self):
        repository = self.createRepository()
        repository.add({ 'Name': 'Test1', 'IsPercentage': True })
        repository.add({ 'Name': 'Test2', 'IsPercentage': True })
        repository.add({ 'Name': 'Test3', 'IsPercentage': True })
        actual = repository.getById(3)
        self.assertEqual(actual, { 'Id': 3, 'Name': 'Test3', 'IsPercentage': True })
        repository = None

    def testGetId(self):
        repository = self.createRepository()
        repository.add({ 'Name': 'Test1', 'IsPercentage': True })
        repository.add({ 'Name': 'Test2', 'IsPercentage': True })
        repository.add({ 'Name': 'Test3', 'IsPercentage': True })
        actual = repository.getId({ 'Name': 'Test3', 'IsPercentage': True })
        self.assertEqual(actual, 3)
        repository = None

    def testGetByIdException(self):
        repository = self.createRepository()
        try:
            repository.getById(0)
            self.fail()
        except Exception:
            pass
        repository = None

    def testGetIdException(self):
        repository = self.createRepository()
        try:
            repository.getId({ 'Name': 'Test1', 'IsPercentage': True })
            self.fail()
        except Exception:
            pass
        repository = None

if __name__ == '__main__':
    unittest.main()