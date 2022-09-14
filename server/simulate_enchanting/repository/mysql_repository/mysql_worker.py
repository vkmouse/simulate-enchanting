import MySQLdb

class MySQLWorker:
    def connect(self):
        self.__conn = MySQLdb.connect(
            host='jwp63667.mysql.pythonanywhere-services.com',
            user='jwp63667',
            passwd='jwp63667jwp63667',
            db='jwp63667$default',
            connect_timeout=1)
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
        if MySQLWorker.__isAvailable == None:
            try:
                __db = MySQLWorker()
                __db.connect()
                __db.close()
                MySQLWorker.__isAvailable = True
            except:
                MySQLWorker.__isAvailable = False
        return MySQLWorker.__isAvailable
