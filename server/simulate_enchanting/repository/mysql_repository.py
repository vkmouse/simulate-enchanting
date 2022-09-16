from typing import final
from simulate_enchanting.repository.repository import Repository
from simulate_enchanting.repository.mysql_worker import MySQLWorker

class MySQLRepository(Repository):
    def __init__(self, worker: MySQLWorker, testMode=False):
        self._worker = worker
        self._testMode = testMode

    def __del__(self):
        if self._testMode:
            self._dropTable()

    def initialize(self):
        self._createTable()

    def add(self, __object):
        data = list(map(lambda prop: __object[prop], self._props))
        self._worker.cursorExecute(self._addSQL, data)

    def getById(self, __id: int):
        data = (__id,)
        self._worker.cursorExecute(self._getByIdSQL, data)
        row = self._worker.cursorFetchOne()
        result = { 'Id': row[0] }
        for i, prop in enumerate(self._props):
            result[prop] = row[i + 1]
        return result

    def getId(self, __object) -> int:
        data = list(map(lambda prop: __object[prop], self._props))
        self._worker.cursorExecute(self._getIdSQL, data)
        row = self._worker.cursorFetchOne()
        return row[0]

    def getAll(self):
        self._worker.cursorExecute(self._getAllSQL)
        props = ['Id'] + self._props
        results = []
        for row in self._worker.cursorFetchAll():
            result = {}
            for i, prop in enumerate(props):
                result[prop] = row[i]
            results.append(result)
        return results

    @property
    def _createTableSQL(self) -> str:
        pass

    @property
    def _tableName(self) -> str:
        pass

    @property
    def _props(self) -> list:
        pass

    @property
    def _floatProps(self) -> list:
        return []

    @property
    def _addSQL(self):
        # prop1, ..., propn
        commaSeparatedProps = self.__combineProps(
            '{prop}, ',
            '{prop}'
        )

        # %s AS prop1, ..., %s As propn
        aliasProps = self.__combineProps(
            '%s AS {prop}, ',
            '%s AS {prop}'
        )

        # prop1 = {varName}.prop1 AND ... propn = {varName}.propn
        condition = self.__combineProps(
            '{prop} = NewValue.{prop} AND ',
            '{prop} = NewValue.{prop}'
        )
        for prop in self._floatProps:
            condition = condition.replace(
                '{prop} = NewValue.{prop}'.format(prop=prop), 
                'ABS(NewValue.{prop} - {prop}) < 0.0001'.format(prop=prop)
            )

        return '''
            INSERT INTO {tableName} ({commaSeparatedProps}) (
                SELECT * FROM (
                    SELECT {aliasProps}
                ) AS NewValue
                WHERE NOT EXISTS(
                    SELECT * FROM {tableName}
                    WHERE {condition}
                )
            );
        '''.format(
                aliasProps=aliasProps,
                commaSeparatedProps=commaSeparatedProps,
                condition=condition,
                tableName=self._tableName
            )

    @final
    @property
    def _getByIdSQL(self):
        return '''
            SELECT * FROM {tableName}
            WHERE Id = %s
        '''.format(tableName=self._tableName)

    @final
    @property
    def _getIdSQL(self):
        # prop1 = %s AND ... propn = %s
        condition = self.__combineProps(
            '{prop} = %s AND ',
            '{prop} = %s'
        )
        for prop in self._floatProps:
            condition = condition.replace(
                '{} = %s'.format(prop), 
                'ABS({} - %s) < 0.0001'.format(prop)
            )

        return '''
            SELECT Id FROM {tableName} 
            WHERE {condition}
        '''.format(
                tableName=self._tableName, 
                condition=condition
            )

    @property
    def _getAllSQL(self):
        return 'SELECT * FROM {}'.format(self._tableName)

    @final
    def _createTable(self):
        self._worker.connQuery(self._createTableSQL)

    @final
    def _dropTable(self):
        sql = 'DROP TABLE {tableName}'.format(tableName=self._tableName)
        self._worker.connQuery(sql)

    def __combineProps(self, exceptLast, last):
        result = ''
        for prop in self._props[:len(self._props) - 1]:
           result += exceptLast.format(prop=prop)
        result += last.format(prop=self._props[-1])
        return result