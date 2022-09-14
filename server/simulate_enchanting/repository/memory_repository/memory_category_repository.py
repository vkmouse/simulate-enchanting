from simulate_enchanting.core import EnchantmentCategory
from simulate_enchanting.repository.memory_repository.memory_repository import MemoryRepository

class MemoryCategoryRepository(MemoryRepository):
    def _compare(self, lhs, rhs) -> bool:
        return lhs['IsPercentage'] == rhs['IsPercentage'] and lhs['Name'] == rhs['Name']