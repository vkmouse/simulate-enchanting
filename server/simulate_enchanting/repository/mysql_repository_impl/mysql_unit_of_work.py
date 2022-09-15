from simulate_enchanting.repository.mysql_repository_impl.mysql_attribute_repository import MySQLAttributeRepository
from simulate_enchanting.repository.mysql_repository_impl.mysql_category_repository import MySQLCategoryRepository
from simulate_enchanting.repository.mysql_repository_impl.mysql_range_repository import MySQLRangeRepository
from simulate_enchanting.repository.mysql_repository_impl.mysql_row_repository import MySQLRowRepository
from simulate_enchanting.repository.mysql_repository_impl.mysql_serial_repository import MySQLSerialRepository
from simulate_enchanting.repository.mysql_worker import MySQLWorker
from simulate_enchanting.repository.unit_of_work import UnitOfWork

class MySQLUnitOfWork(UnitOfWork):
    def __init__(self, testMode=False):
        self.__testMode = testMode

    def initialize(self):
        self.__worker = MySQLWorker()
        self.__worker.connect()
        super().initialize()

    def _createAttributeRepository(self):
        repository = MySQLAttributeRepository(self.__worker, self.__testMode)
        repository.initialize()
        return super()._createAttributeRepository()

    def _createCategoryRepository(self):
        repository = MySQLCategoryRepository(self.__worker, self.__testMode)
        repository.initialize()
        return repository

    def _createRangeRepository(self):
        repository = MySQLRangeRepository(self.__worker, self.__testMode)
        repository.initialize()
        return repository

    def _createRowRepository(self):
        repository = MySQLRowRepository(self.__worker, self.__testMode)
        repository.initialize()
        return repository

    def _createSerialRepository(self):
        repository = MySQLSerialRepository(self.__worker, self.__testMode)
        repository.initialize()
        return repository
