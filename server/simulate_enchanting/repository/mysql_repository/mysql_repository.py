from typing import final
from simulate_enchanting.repository.mysql_repository.mysql_worker import MySQLWorker

class MySQLRepository:
    def __init__(self, worker: MySQLWorker):
        self.worker = worker

    @property
    def _tableName(self):
        pass

    @final
    def _dropTable(self, tableName):
        sql = 'DROP TABLE {}'.format(self.tableName)
        self.worker.connQuery(sql)
