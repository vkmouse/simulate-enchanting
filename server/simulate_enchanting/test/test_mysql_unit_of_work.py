import unittest
from simulate_enchanting.repository import MySQLUnitOfWork, MySQLWorker

class TestMySQLUnitOfWork(unittest.TestCase):
    @unittest.skipIf(not MySQLWorker.isAvailable(), 'MySQL is not available')
    def testRepositoryType(self):
        unitOfWork = MySQLUnitOfWork(testMode=True)
        unitOfWork.initialize()
        self.assertTrue(str(type(unitOfWork.attributeRepository)).find('MySQLAttributeRepository') > 0)
        self.assertTrue(str(type(unitOfWork.categoryRepository)).find('MySQLCategoryRepository') > 0)
        self.assertTrue(str(type(unitOfWork.rangeRepository)).find('MySQLRangeRepository') > 0)
        self.assertTrue(str(type(unitOfWork.rowRepository)).find('MySQLRowRepository') > 0)
        self.assertTrue(str(type(unitOfWork.serialRepository)).find('MySQLSerialRepository') > 0)

if __name__ == '__main__':
    unittest.main()