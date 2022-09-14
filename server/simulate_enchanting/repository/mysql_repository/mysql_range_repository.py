from simulate_enchanting.repository.mysql_repository.mysql_repository import MySQLRepository

class MySQLRangeRepository(MySQLRepository):
    @property
    def _createTableSQL(self) -> str:
        return '''
            CREATE TABLE IF NOT EXISTS EnchantmentRange (
                Id              INT     NOT NULL    AUTO_INCREMENT,
                Start           INT     NOT NULL,
                Stop            INT     NOT NULL,
                Step            INT     NOT NULL,
                PRIMARY KEY(Id)
            );
        '''.format(self._tableName)

    @property
    def _tableName(self) -> str:
        if self._testMode:
            return 'TestEnchantmentRange'
        else:
            return 'EnchantmentRange'

    @property
    def _props(self) -> list:
        return ['Start', 'Stop', 'Step']
