from simulate_enchanting.core import EnchantmentCategory
from simulate_enchanting.repository import MySQLWorker
from simulate_enchanting.repository.mysql_repository.mysql_repository import MySQLRepository

class MySQLCategoryRepository(MySQLRepository):
    def __init__(self, worker: MySQLWorker, testMode=False):
        super().__init__(worker)
        self.__testMode = testMode
        self.__createTable()

    def __del__(self):
        if self.__testMode:
            self._dropTable()
        self._worker.close()

    @property
    def _tableName(self) -> str:
        if self.__testMode:
            return 'TestEnchantmentCategory'
        else:
            return 'EnchantmentCategory'

    @property
    def _props(self) -> list:
        return ['Name', 'IsPercentage']

    def __createTable(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS {} (
                Id              INT             NOT NULL    AUTO_INCREMENT,
                Name            VARCHAR(255)    NOT NULL,
                IsPercentage    BOOLEAN         NOT NULL,
                PRIMARY KEY(Id)
            );
        '''.format(self._tableName)
        self._worker.connQuery(sql)
