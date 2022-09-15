from simulate_enchanting.repository.mysql_repository import MySQLRepository
from simulate_enchanting.repository.mysql_worker import MySQLWorker

class MySQLAttributeRepository(MySQLRepository):
    def __init__(self, 
        worker: MySQLWorker, 
        testMode=False,
        categoryTableName='EnchantmentCategory',
        rangeTableName='EnchantmentRange',
        rowTableName='EnchantmentRow',
        serialTableName='EnchantmentSerial',
    ):
        super().__init__(worker, testMode)
        self.__categoryTableName = categoryTableName
        self.__rangeTableName = rangeTableName
        self.__rowTableName = rowTableName
        self.__serialTableName = serialTableName

    @property
    def _createTableSQL(self) -> str:
        return '''
            CREATE TABLE IF NOT EXISTS {tableName} (
                Id          INT     NOT NULL    AUTO_INCREMENT,
                Probability FLOAT   NOT NULL,
                CategoryId  INT     NOT NULL,
                RangeId     INT     NOT NULL,
                RowId       INT     NOT NULL,
                SerialId    INT     NOT NULL,
                PRIMARY KEY(Id),
                FOREIGN KEY(CategoryId) REFERENCES {categoryTableName}(Id),
                FOREIGN KEY(RangeId) REFERENCES {rangeTableName}(Id),
                FOREIGN KEY(RowId) REFERENCES {rowTableName}(Id),
                FOREIGN KEY(SerialId) REFERENCES {serialTableName}(Id)
            );
        '''.format(
                tableName=self._tableName,
                categoryTableName=self.__categoryTableName,
                rangeTableName=self.__rangeTableName,
                rowTableName=self.__rowTableName,
                serialTableName=self.__serialTableName
            )

    @property
    def _tableName(self) -> str:
        if self._testMode:
            return 'TestEnchantmentAttribute'
        else:
            return 'EnchantmentAttribute'

    @property
    def _props(self) -> list:
        return ['Probability', 'CategoryId', 'RangeId', 'RowId', 'SerialId']
