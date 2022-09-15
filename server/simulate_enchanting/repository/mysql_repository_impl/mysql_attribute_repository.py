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

    def add(self, __object):
        data = [
            __object['Probability'],
            __object['Category']['Name'],
            __object['Category']['IsPercentage'],
            __object['Range']['Start'],
            __object['Range']['Stop'],
            __object['Range']['Step'],
            __object['Row']['Probability'],
            __object['Row']['RowNumber'],
            __object['Serial']['Name'],
            __object['Serial']['Des'],
            __object['Serial']['Url'],
            __object['Serial']['API'],
        ]
        self._worker.cursorExecute(self._addSQL, data)

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

    @property
    def _floatProps(self) -> list:
        return ['Probability']

    @property
    def _addSQL(self):
        return '''
            INSERT INTO {tableName} (Probability, CategoryId, RangeId, RowId, SerialId) (
                SELECT * FROM (
                    SELECT %s AS Probability, (
                        SELECT Id FROM {categoryTableName} WHERE Name = %s AND IsPercentage = %s
                    ) AS CategoryId, (
                        (SELECT Id FROM {rangeTableName} WHERE Start = %s AND Stop = %s AND Step = %s)
                    ) AS RangeId, (
                        (SELECT Id FROM {rowTableName} WHERE ABS(Probability - %s) < 0.0001 AND RowNumber = %s)
                    ) AS RowId, (
                        (SELECT Id FROM {serialTableName} WHERE Name = %s AND Des = %s AND Url = %s AND API = %s)
                    ) AS SerialId
                ) AS NewValue
                WHERE NOT EXISTS(
                    SELECT * FROM {tableName}
                    WHERE ABS(NewValue.Probability - Probability) < 0.0001 AND CategoryId = NewValue.CategoryId AND RangeId = NewValue.RangeId AND RowId = NewValue.RowId AND SerialId = NewValue.SerialId
                )
            );
        '''.format(
                tableName=self._tableName,
                categoryTableName=self.__categoryTableName,
                rangeTableName=self.__rangeTableName,
                rowTableName=self.__rowTableName,
                serialTableName=self.__serialTableName
            )