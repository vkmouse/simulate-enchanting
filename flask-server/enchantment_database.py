from unicodedata import category
from core import EnchantmentProbabilityNotice, EnchantmentCategory, EnchantmentSerial, EnchantmentRange, EnchantmentRow, EnchantableAttributeProbability
from typing import List, TypedDict, final
from enchantment_converter import EnchantmentProbabilityNoticeConverter
import MySQLdb

class EnchantableAttributeProbabilityDb(TypedDict): 
    CategoryId: int
    RangeId: int
    SerialId: int
    Probability: float
    RowId: int

class EnchantmentDatabase:
    @property
    def serials(self) -> List[EnchantmentSerial]:
        return []

    @property
    def categories(self) -> List[EnchantmentCategory]:
        return []

    @property
    def ranges(self) -> List[EnchantmentRange]:
        return []

    @property
    def rows(self) -> List[EnchantmentRange]:
        return []

    @property
    def attributeProbabilities(self) -> List[EnchantableAttributeProbability]:
        return []

    @final
    def appendNotice(self, value: EnchantmentProbabilityNotice):
        converter = EnchantmentProbabilityNoticeConverter(value)
        converter.convert()
        self.appendSerial(converter.serial)
        for category in converter.categories:
            self.appendCategory(category)
        for range in converter.ranges:
            self.appendRange(range)
        for row in converter.rows:
            self.appendRows(row)
        for attributeProbability in converter.attributeProbabilities:
            self.appendAttributeProbability(attributeProbability)

    def appendSerial(self, value: EnchantmentSerial):
        pass

    def appendCategory(self, value: EnchantmentCategory):
        pass

    def appendRange(self, value: EnchantmentRange):
        pass

    def appendRows(self, value: EnchantmentRow):
        pass

    def appendAttributeProbability(self, value: EnchantableAttributeProbability):
        pass

    def initial(self):
        pass

class MemoryEnchantmentDatabase(EnchantmentDatabase):
    __serials: List[EnchantmentSerial]
    __categories: List[EnchantmentCategory]
    __ranges: List[EnchantmentRange]
    __rows: List[EnchantmentRow]
    __attributeProbabilities: List[EnchantableAttributeProbabilityDb]

    def initial(self):
        self.__serials = []
        self.__categories = []
        self.__ranges = []
        self.__rows = []
        self.__attributeProbabilities = []

    @property
    def serials(self) -> List[EnchantmentSerial]:
        return self.__serials

    @property
    def categories(self) -> List[EnchantmentCategory]:
        return self.__categories

    @property
    def ranges(self) -> List[EnchantmentRange]:
        return self.__ranges

    @property
    def rows(self) -> List[EnchantmentRow]:
        return self.__rows

    @property
    def attributeProbabilities(self) -> List[EnchantableAttributeProbability]:
        return list(map(lambda x: {
            'Attribute': {
                'Category': self.categories[x['CategoryId']],
                'Range': self.ranges[x['RangeId']],
            },
            'Probability': x['Probability'],
            'Row': self.rows[x['RowId']],
            'Serial': self.serials[x['SerialId']]
        }, self.__attributeProbabilities))

    def appendSerial(self, value: EnchantmentSerial):
        if (value not in self.__serials):
            self.__serials.append(value)

    def appendCategory(self, value: EnchantmentCategory):
        if (value not in self.__categories):
            self.__categories.append(value)

    def appendRange(self, value: EnchantmentRange):
        if (value not in self.__ranges):
            self.__ranges.append(value)

    def appendRows(self, value: EnchantmentRow):
        if (value not in self.__rows):
            self.__rows.append(value)

    def appendAttributeProbability(self, value: EnchantableAttributeProbability):
        newValue: EnchantableAttributeProbabilityDb = {
            'CategoryId': self.categories.index(value['Attribute']['Category']),
            'RangeId': self.ranges.index(value['Attribute']['Range']),
            'SerialId': self.serials.index(value['Serial']),
            'Probability': value['Probability'],
            'RowId': self.rows.index(value['Row']),
        }
        if (newValue not in self.__attributeProbabilities):
            self.__attributeProbabilities.append(newValue)

class MySQLEnchantmentDatabase(EnchantmentDatabase):
    def initial(self):
        conn = MySQLdb.connect(
            host="jwp63667.mysql.pythonanywhere-services.com",
            user="jwp63667",
            passwd="jwp63667jwp63667",
            db="jwp63667$default")

        cur = conn.cursor()

        dbCreate = '''
            CREATE TABLE IF NOT EXISTS EnchantmentCategory (
                Id              INT             NOT NULL    AUTO_INCREMENT,
                Name            VARCHAR(255)    NOT NULL,
                IsPercentage    BOOLEAN         NOT NULL,
                PRIMARY KEY(Id)
            );

            CREATE TABLE IF NOT EXISTS EnchantmentRange (
                Id              INT     NOT NULL    AUTO_INCREMENT,
                Start           INT     NOT NULL,
                Stop            INT     NOT NULL,
                Step            INT     NOT NULL,
                PRIMARY KEY(Id)
            );

            CREATE TABLE IF NOT EXISTS EnchantmentSerial (
                Id      INT             NOT NULL    AUTO_INCREMENT,
                Name    VARCHAR(255)    NOT NULL,
                Des     VARCHAR(255)    NOT NULL,
                Url     VARCHAR(255)    NOT NULL,
                API     VARCHAR(255)    NOT NULL,
                PRIMARY KEY(Id)
            );

            CREATE TABLE IF NOT EXISTS EnchantmentRow (
                Id          INT     NOT NULL    AUTO_INCREMENT,
                RowNumber   INT     NOT NULL,
                Probability FLOAT   NOT NULL,
                PRIMARY KEY(Id)
            );

            CREATE TABLE IF NOT EXISTS EnchantableAttributeProbability (
                Id          INT     NOT NULL    AUTO_INCREMENT,
                Probability FLOAT   NOT NULL,
                CategoryId  INT     NOT NULL,
                RangeId     INT     NOT NULL,
                SerialId    INT     NOT NULL,
                RowId       INT     NOT NULL,
                PRIMARY KEY(Id),
                FOREIGN KEY(CategoryId) REFERENCES EnchantmentCategory(Id),
                FOREIGN KEY(RangeId) REFERENCES EnchantmentRange(Id),
                FOREIGN KEY(SerialId) REFERENCES EnchantmentSerial(Id),
                FOREIGN KEY(RowId) REFERENCES EnchantmentRow(Id)
            );
        '''
        cur.execute(dbCreate)

def createMemoryEnchantmentDatabase() -> EnchantmentDatabase:
    db = MemoryEnchantmentDatabase()
    db.initial()
    return db

def createMySQLEnchantmentDatabase() -> EnchantmentDatabase:
    db = MySQLEnchantmentDatabase()
    db.initial()
    return db