from sqlite3 import connect
import MySQLdb

class MySQLRepository:
    def connect(self):
        self.__conn = MySQLdb.connect(
            host='jwp63667.mysql.pythonanywhere-services.com',
            user='jwp63667',
            passwd='jwp63667jwp63667',
            db='jwp63667$default',
            connect_timeout=0.5)
        self.__cursor = self.__conn.cursor()

    def connQuery(self, sql):
        self.__conn.query(sql)

    def cursorExecute(self, sql, data):
        self.__cursor.execute(sql, data)
        self.__conn.commit()

    def cursorFetchOne(self):
        row = self.__cursor.fetchone()
        if row:
            return row
        else:
            raise Exception('[MySQLRepository] object is not existed')

    def close(self):
        self.__cursor.close()
        self.__conn.close()

    __isAvailable = None
    @staticmethod
    def isAvailable():
        if MySQLRepository.__isAvailable == None:
            try:
                __db = MySQLRepository()
                __db.connect()
                __db.close()
                MySQLRepository.__isAvailable = True
            except:
                MySQLRepository.__isAvailable = False
        return MySQLRepository.__isAvailable
