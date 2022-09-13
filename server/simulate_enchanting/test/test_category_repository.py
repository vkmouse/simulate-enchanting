from functools import cache
import unittest
from simulate_enchanting.repository import MemoryCategoryRepository

class TestCategoryRepository(unittest.TestCase):
    def createRepository(self):
        return MemoryCategoryRepository()

    def testAdd(self):
        repository = self.createRepository()
        expected = { 'Name': 'Test0', 'IsPercentage': True }
        repository.add(expected)
        actual = repository.getById(0)
        self.assertEqual(expected, actual)

    def testGetById(self):
        repository = self.createRepository()
        repository.add({ 'Name': 'Test0', 'IsPercentage': True })
        repository.add({ 'Name': 'Test1', 'IsPercentage': True })
        repository.add({ 'Name': 'Test2', 'IsPercentage': True })
        actual = repository.getById(2)
        self.assertEqual(actual, { 'Id': 2, 'Name': 'Test2', 'IsPercentage': True })

    def testGetId(self):
        repository = self.createRepository()
        repository.add({ 'Name': 'Test0', 'IsPercentage': True })
        repository.add({ 'Name': 'Test1', 'IsPercentage': True })
        repository.add({ 'Name': 'Test2', 'IsPercentage': True })
        actual = repository.getId({ 'Name': 'Test2', 'IsPercentage': True })
        self.assertEqual(actual, 2)

    def testGetByIdException(self):
        repository = self.createRepository()
        try:
            repository.getById(0)
            self.fail()
        except Exception:
            pass

    def testGetIdException(self):
        repository = self.createRepository()
        try:
            repository.getId({ 'Name': 'Test1', 'IsPercentage': True })
            self.fail()
        except Exception:
            pass

if __name__ == '__main__':
    unittest.main()