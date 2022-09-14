from simulate_enchanting.core import EnchantmentCategory
from simulate_enchanting.repository.memory_repository.memory_repository import MemoryRepository

class MemoryCategoryRepository(MemoryRepository):
    @property
    def _props(self):
        return ['Name', 'IsPercentage']