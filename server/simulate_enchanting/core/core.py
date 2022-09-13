from typing import TypedDict

class EnchantmentCategory(TypedDict):
    Name: str
    IsPercentage: bool

class EnchantmentRange(TypedDict):
    Start: int
    Stop: int
    Step: int
    
class EnchantmentRow(TypedDict):
    Probability: float
    RowNumber: int

class EnchantmentSerial(TypedDict):
    Name: str
    Des: str
    Url: str
    API: str

class EnchantableAttribute(TypedDict):
    Probability: float
    Category: EnchantmentCategory
    Range: EnchantmentRange
    Row: EnchantmentRow
    Serial: EnchantmentSerial
