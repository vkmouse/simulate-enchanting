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

    def getById(self, __id: int):
        data = (__id,)
        self._worker.cursorExecute(self._getByIdSQL, data)
        row = self._worker.cursorFetchOne()
        result = { 
            'Id': row[0],
            'Probability': row[1],
            'Category': { 'Id': row[2], 'Name': row[3], 'IsPercentage': row[4] },
            'Range': { 'Id': row[5], 'Start': row[6], 'Stop': row[7], 'Step': row[8] },
            'Row': { 'Id': row[9], 'Probability': row[10], 'RowNumber': row[11] },
            'Serial': { 'Id': row[12], 'Name': row[13], 'Des': row[14], 'Url': row[15], 'API': row[16] },
        }
        return result

    def getId(self, __object) -> int:
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
        self._worker.cursorExecute(self._getIdSQL, data)
        row = self._worker.cursorFetchOne()
        return row[0]

    def getAll(self):
        self._worker.cursorExecute(self._getAllSQL)
        results = []
        for row in self._worker.cursorFetchAll():
            results.append({ 
                'Id': row[0],
                'Probability': row[1],
                'Category': { 'Id': row[2], 'Name': row[3], 'IsPercentage': row[4] },
                'Range': { 'Id': row[5], 'Start': row[6], 'Stop': row[7], 'Step': row[8] },
                'Row': { 'Id': row[9], 'Probability': row[10], 'RowNumber': row[11] },
                'Serial': { 'Id': row[12], 'Name': row[13], 'Des': row[14], 'Url': row[15], 'API': row[16] },
            })
        return results

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

    @property
    def _getByIdSQL(self):
        return '''
            SELECT  _attribute.Id, 
                    _attribute.Probability, 
                    _category.Id,
                    _category.Name, 
                    _category.IsPercentage,
                    _range.Id,
                    _range.Start,
                    _range.Stop,
                    _range.Step,
                    _row.Id,
                    _row.Probability,
                    _row.RowNumber,
                    _serial.Id,
                    _serial.Name,
                    _serial.Des,
                    _serial.Url,
                    _serial.API
                    FROM {tableName} _attribute
                    INNER JOIN {categoryTableName} AS _category 
                        ON _category.Id = _attribute.CategoryId
                    INNER JOIN {rangeTableName} AS _range
                        ON _range.Id = _attribute.RangeId
                    INNER JOIN {rowTableName} AS _row
                        ON _row.Id = _attribute.RowId
                    INNER JOIN {serialTableName} AS _serial
                        ON _serial.Id = _attribute.SerialId
                    WHERE _attribute.Id = %s;
        '''.format(
                tableName=self._tableName,
                categoryTableName=self.__categoryTableName,
                rangeTableName=self.__rangeTableName,
                rowTableName=self.__rowTableName,
                serialTableName=self.__serialTableName
            )

    @property
    def _getIdSQL(self):
        return '''
            SELECT _attribute.Id
            FROM {tableName} _attribute
            INNER JOIN {categoryTableName} AS _category 
                ON _category.Id = _attribute.CategoryId
            INNER JOIN {rangeTableName} AS _range
                ON _range.Id = _attribute.RangeId
            INNER JOIN {rowTableName} AS _row
                ON _row.Id = _attribute.RowId
            INNER JOIN {serialTableName} AS _serial
                ON _serial.Id = _attribute.SerialId
            WHERE ABS(_attribute.Probability - %s) < 0.0001 AND
                  _category.Name = %s AND 
                  _category.IsPercentage = %s AND
                  _range.Start = %s AND
                  _range.Stop = %s AND
                  _range.Step = %s AND
                  ABS(_row.Probability - %s) < 0.0001 AND
                  _row.RowNumber = %s AND
                  _serial.Name = %s AND
                  _serial.Des = %s AND
                  _serial.Url = %s AND
                  _serial.API = %s;
        '''.format(
                tableName=self._tableName,
                categoryTableName=self.__categoryTableName,
                rangeTableName=self.__rangeTableName,
                rowTableName=self.__rowTableName,
                serialTableName=self.__serialTableName
            )

    @property
    def _getAllSQL(self):
        return '''
            SELECT  _attribute.Id, 
                    _attribute.Probability, 
                    _category.Id,
                    _category.Name, 
                    _category.IsPercentage,
                    _range.Id,
                    _range.Start,
                    _range.Stop,
                    _range.Step,
                    _row.Id,
                    _row.Probability,
                    _row.RowNumber,
                    _serial.Id,
                    _serial.Name,
                    _serial.Des,
                    _serial.Url,
                    _serial.API
            FROM {tableName} _attribute
            INNER JOIN {categoryTableName} AS _category 
                ON _category.Id = _attribute.CategoryId
            INNER JOIN {rangeTableName} AS _range
                ON _range.Id = _attribute.RangeId
            INNER JOIN {rowTableName} AS _row
                ON _row.Id = _attribute.RowId
            INNER JOIN {serialTableName} AS _serial
                ON _serial.Id = _attribute.SerialId
        '''.format(
                tableName=self._tableName,
                categoryTableName=self.__categoryTableName,
                rangeTableName=self.__rangeTableName,
                rowTableName=self.__rowTableName,
                serialTableName=self.__serialTableName
            )