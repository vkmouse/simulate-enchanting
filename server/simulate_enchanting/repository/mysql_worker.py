from sqlite3 import connect
import MySQLdb

class MySQLWorker:
    def __init__(self):
        self.__conn = None
        self.__cursor = None

    def __del__(self):
        self.close()

    def connect(self):
        if not self.__isConnected():
            self.__conn = MySQLdb.connect(
                host='jwp63667.mysql.pythonanywhere-services.com',
                user='jwp63667',
                passwd='jwp63667jwp63667',
                db='jwp63667$default',
                connect_timeout=1)
            self.__cursor = self.__conn.cursor()

    def connQuery(self, sql):
        self.connect()
        self.__conn.query(sql)

    def cursorExecute(self, sql, data=None):
        self.connect()
        self.__cursor.execute(sql, data)
        self.__conn.commit()

    def cursorFetchOne(self):
        self.connect()
        row = self.__cursor.fetchone()
        if row:
            return row
        else:
            raise Exception('[MySQLRepository] object is not existed')

    def cursorFetchAll(self):
        self.connect()
        return self.__cursor.fetchall()

    def close(self):
        if self.__cursor != None:
            self.__cursor.close()
            self.__cursor = None
        if self.__conn != None:
            self.__conn.close()
            self.__conn = None

    def __isConnected(self):
        try: 
            self.__conn.ping()
            return True
        except:
            return False

    __isAvailable = None
    @staticmethod
    def isAvailable():
        if MySQLWorker.__isAvailable == None:
            try:
                __db = MySQLWorker()
                __db.connect()
                __db.close()
                MySQLWorker.__isAvailable = True
            except:
                MySQLWorker.__isAvailable = False
        return MySQLWorker.__isAvailable
