from simulate_enchanting.repository.mysql_repository import MySQLRepository

class MySQLRowRepository(MySQLRepository):
    @property
    def _createTableSQL(self) -> str:
        return '''
            CREATE TABLE IF NOT EXISTS {} (
                Id          INT     NOT NULL    AUTO_INCREMENT,
                Probability FLOAT   NOT NULL,
                RowNumber   INT     NOT NULL,
                PRIMARY KEY(Id)
            );
        '''.format(self._tableName)

    @property
    def _tableName(self) -> str:
        if self._testMode:
            return 'TestEnchantmentRow'
        else:
            return 'EnchantmentRow'

    @property
    def _props(self) -> list:
        return ['Probability', 'RowNumber']
