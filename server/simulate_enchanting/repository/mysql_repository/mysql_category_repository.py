import MySQLdb
from simulate_enchanting.core import EnchantmentCategory
from simulate_enchanting.repository.repository import Repository

class MySQLCategoryRepository:
    def __init__(self, testMode=False):
        self.__testMode = testMode
        self.__connect()
        self.__createTable()

    def __del__(self):
        if self.__testMode:
            self.__dropTable()
        self.__cursor.close()
        self.__conn.close()

    def add(self, __object: EnchantmentCategory):
        data = (__object['Name'], __object['IsPercentage'])
        self.__cursorExecute(self.__addSQL, data)

    def getById(self, __id: int) -> EnchantmentCategory:
        data = (__id,)
        self.__cursorExecute(self.__getByIdSQL, data)
        row = self.__cursorFetchOne()
        return { 'Id': row[0], 'Name': row[1], 'IsPercentage': bool(row[2]) }

    def getId(self, __object: EnchantmentCategory) -> int:
        data = (__object['Name'], __object['IsPercentage'])
        self.__cursorExecute(self.__getIdSQL, data)
        row = self.__cursorFetchOne()
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

    def __connect(self):
        self.__conn = MySQLdb.connect(
            host='jwp63667.mysql.pythonanywhere-services.com',
            user='jwp63667',
            passwd='jwp63667jwp63667',
            db='jwp63667$default')
        self.__cursor = self.__conn.cursor()

    def __createTable(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS {} (
                Id              INT             NOT NULL    AUTO_INCREMENT,
                Name            VARCHAR(255)    NOT NULL,
                IsPercentage    BOOLEAN         NOT NULL,
                PRIMARY KEY(Id)
            );
        '''.format(self.__tableName)
        self.__connQuery(sql)

    def __dropTable(self):
        sql = 'DROP TABLE {}'.format(self.__tableName)
        self.__connQuery(sql)

    def __connQuery(self, sql):
        self.__conn.query(sql)

    def __cursorExecute(self, sql, data):
        self.__cursor.execute(sql, data)
        self.__conn.commit()

    def __cursorFetchOne(self):
        row = self.__cursor.fetchone()
        if row:
            return row
        else:
            raise Exception('[MySQLCategoryRepository] object is not existed')
