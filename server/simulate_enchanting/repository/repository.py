import abc
 
class Repository(metaclass=abc.ABCMeta):
    def initialize(self):
        return NotImplemented

    def add(self, obj):
        return NotImplemented
    
    def getById(self, id: int):
        return NotImplemented

    def getId(self, obj):
        return NotImplemented

    def getAll(self):
        return NotImplemented