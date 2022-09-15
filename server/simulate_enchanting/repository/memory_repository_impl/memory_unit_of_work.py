from simulate_enchanting.repository.unit_of_work import UnitOfWork
from simulate_enchanting.repository.memory_repository_impl.memory_repositories import MemoryCategoryRepository, MemoryRangeRepository, MemoryRowRepository, MemorySerialRepository

class MemoryUnitOfWork(UnitOfWork):
    def _createCategoryRepository(self):
        return MemoryCategoryRepository()

    def _createRangeRepository(self):
        return MemoryRangeRepository()

    def _createRowRepository(self):
        return MemoryRowRepository()

    def _createSerialRepository(self):
        return MemorySerialRepository()
