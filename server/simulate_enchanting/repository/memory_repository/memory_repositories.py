from simulate_enchanting.repository.memory_repository.memory_repository import MemoryRepository

class MemoryCategoryRepository(MemoryRepository):
    @property
    def _props(self):
        return ['Name', 'IsPercentage']

class MemoryRangeRepository(MemoryRepository):
    @property
    def _props(self):
        return ['Start', 'Stop', 'Step']

class MemoryRowRepository(MemoryRepository):
    @property
    def _props(self):
        return ['Probability', 'RowNumber']

class MemorySerialRepository(MemoryRepository):
    @property
    def _props(self):
        return ['Name', 'Des', 'Url', 'API']