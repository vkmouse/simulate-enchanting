from simulate_enchanting.repository.unit_of_work import UnitOfWork
from simulate_enchanting.repository.memory_repository_impl.memory_repositories import MemoryCategoryRepository, MemoryRangeRepository, MemoryRowRepository, MemorySerialRepository
from simulate_enchanting.repository.memory_repository_impl.memory_attribute_repository import MemoryAttributeRepository

class MemoryUnitOfWork(UnitOfWork):
    def _createAttributeRepository(self):
        repository = MemoryAttributeRepository(self)
        repository.initialize()
        return repository

    def _createCategoryRepository(self):
        repository = MemoryCategoryRepository()
        repository.initialize()
        return repository

    def _createRangeRepository(self):
        repository = MemoryRangeRepository()
        repository.initialize()
        return repository

    def _createRowRepository(self):
        repository = MemoryRowRepository()
        repository.initialize()
        return repository

    def _createSerialRepository(self):
        repository = MemorySerialRepository()
        repository.initialize()
        return repository
