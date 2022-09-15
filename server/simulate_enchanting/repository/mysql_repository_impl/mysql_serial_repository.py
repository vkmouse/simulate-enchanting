from simulate_enchanting.repository.mysql_repository import MySQLRepository

class MySQLSerialRepository(MySQLRepository):
    @property
    def _createTableSQL(self) -> str:
        return '''
            CREATE TABLE IF NOT EXISTS {} (
                Id      INT             NOT NULL    AUTO_INCREMENT,
                Name    VARCHAR(255)    NOT NULL,
                Des     VARCHAR(255)    NOT NULL,
                Url     VARCHAR(255)    NOT NULL,
                API     VARCHAR(255)    NOT NULL,
                PRIMARY KEY(Id)
            );
        '''.format(self._tableName)

    @property
    def _tableName(self) -> str:
        if self._testMode:
            return 'TestEnchantmentSerial'
        else:
            return 'EnchantmentSerial'

    @property
    def _props(self) -> list:
        return ['Name', 'Des', 'Url', 'API']
