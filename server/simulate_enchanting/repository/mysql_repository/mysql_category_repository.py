from simulate_enchanting.repository.mysql_repository.mysql_repository import MySQLRepository

class MySQLCategoryRepository(MySQLRepository):
    @property
    def _createTableSQL(self) -> str:
        return '''
            CREATE TABLE IF NOT EXISTS {} (
                Id              INT             NOT NULL    AUTO_INCREMENT,
                Name            VARCHAR(255)    NOT NULL,
                IsPercentage    BOOLEAN         NOT NULL,
                PRIMARY KEY(Id)
            );
        '''.format(self._tableName)

    @property
    def _tableName(self) -> str:
        if self._testMode:
            return 'TestEnchantmentCategory'
        else:
            return 'EnchantmentCategory'

    @property
    def _props(self) -> list:
        return ['Name', 'IsPercentage']
