from simulate_enchanting.repository.mysql_repository import MySQLRepository

class MySQLAttributeRepository(MySQLRepository):
    @property
    def _createTableSQL(self) -> str:
        return '''
            CREATE TABLE IF NOT EXISTS {} (
                Id          INT     NOT NULL    AUTO_INCREMENT,
                Probability FLOAT   NOT NULL,
                CategoryId  INT     NOT NULL,
                RangeId     INT     NOT NULL,
                RowId       INT     NOT NULL,
                SerialId    INT     NOT NULL,
                PRIMARY KEY(Id),
                FOREIGN KEY(CategoryId) REFERENCES EnchantmentCategory(Id),
                FOREIGN KEY(RangeId) REFERENCES EnchantmentRange(Id),
                FOREIGN KEY(RowId) REFERENCES EnchantmentRow(Id),
                FOREIGN KEY(SerialId) REFERENCES EnchantmentSerial(Id)
            );
        '''.format(self._tableName)

    @property
    def _tableName(self) -> str:
        if self._testMode:
            return 'TestEnchantmentAttribute'
        else:
            return 'EnchantmentAttribute'

    @property
    def _props(self) -> list:
        return ['Probability', 'CategoryId', 'RangeId', 'RowId', 'SerialId']
