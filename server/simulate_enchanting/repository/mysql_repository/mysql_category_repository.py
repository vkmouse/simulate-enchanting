from simulate_enchanting.core import EnchantmentCategory
from simulate_enchanting.repository.mysql_repository.mysql_repository import MySQLRepository

class MySQLCategoryRepository:
    def __init__(self, testMode=False):
        self.__testMode = testMode
        self.__db = MySQLRepository()
        self.__db.connect()
        self.__createTable()

    def __del__(self):
        if self.__testMode:
            self.__dropTable()
        self.__db.close()

    def add(self, __object: EnchantmentCategory):
        data = (__object['Name'], __object['IsPercentage'])
        self.__db.cursorExecute(self.__addSQL, data)

    def getById(self, __id: int) -> EnchantmentCategory:
        data = (__id,)
        self.__db.cursorExecute(self.__getByIdSQL, data)
        row = self.__db.cursorFetchOne()
        return { 'Id': row[0], 'Name': row[1], 'IsPercentage': bool(row[2]) }

    def getId(self, __object: EnchantmentCategory) -> int:
        data = (__object['Name'], __object['IsPercentage'])
        self.__db.cursorExecute(self.__getIdSQL, data)
        row = self.__db.cursorFetchOne()
        return row[0]
    
    @property
    def __addSQL(self):
        return '''
            INSERT INTO {tableName} (Name, IsPercentage) (
                SELECT * FROM (
                    SELECT %s AS Name, %s As IsPercentage
                ) AS NewValue 
                WHERE NOT EXISTS(
                    SELECT * FROM {tableName} 
                    WHERE Name = NewValue.Name AND IsPercentage = NewValue.IsPercentage
                )
            );
        '''.format(tableName=self.__tableName)

    @property
    def __getByIdSQL(self):
        return '''
            SELECT * FROM {tableName}
            WHERE Id = %s
        '''.format(tableName=self.__tableName)

    @property
    def __getIdSQL(self):
        return '''
            SELECT Id FROM {tableName} 
            WHERE Name = %s AND IsPercentage = %s
        '''.format(tableName=self.__tableName)

    @property
    def __tableName(self):
        if self.__testMode:
            return 'TestEnchantmentCategory'
        else:
            return 'EnchantmentCategory'

    def __createTable(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS {} (
                Id              INT             NOT NULL    AUTO_INCREMENT,
                Name            VARCHAR(255)    NOT NULL,
                IsPercentage    BOOLEAN         NOT NULL,
                PRIMARY KEY(Id)
            );
        '''.format(self.__tableName)
        self.__db.connQuery(sql)

    def __dropTable(self):
        sql = 'DROP TABLE {}'.format(self.__tableName)
        self.__db.connQuery(sql)
