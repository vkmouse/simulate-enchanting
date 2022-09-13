from typing import TypedDict

class EnchantmentCategory(TypedDict):
    Id: int
    Name: str
    IsPercentage: bool

class EnchantmentRange(TypedDict):
    Id: int
    Start: int
    Stop: int
    Step: int
    
class EnchantmentRow(TypedDict):
    Id: int
    Probability: float
    RowNumber: int

class EnchantmentSerial(TypedDict):
    Id: int
    Name: str
    Des: str
    Url: str
    API: str

class EnchantableAttribute(TypedDict):
    Id: int
    Probability: float
    Category: EnchantmentCategory
    Range: EnchantmentRange
    Row: EnchantmentRow
    Serial: EnchantmentSerial
