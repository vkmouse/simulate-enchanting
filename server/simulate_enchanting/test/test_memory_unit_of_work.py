import unittest
from simulate_enchanting.repository import MemoryUnitOfWork

class TestMemoryUnitOfWork(unittest.TestCase):
    def testRepositoryType(self):
        unitOfWork = MemoryUnitOfWork()
        unitOfWork.initialize()
        self.assertTrue(str(type(unitOfWork.attributeRepository)).find('MemoryAttributeRepository') > 0)
        self.assertTrue(str(type(unitOfWork.categoryRepository)).find('MemoryCategoryRepository') > 0)
        self.assertTrue(str(type(unitOfWork.rangeRepository)).find('MemoryRangeRepository') > 0)
        self.assertTrue(str(type(unitOfWork.rowRepository)).find('MemoryRowRepository') > 0)
        self.assertTrue(str(type(unitOfWork.serialRepository)).find('MemorySerialRepository') > 0)

if __name__ == '__main__':
    unittest.main()