from typing import TypedDict, List

class EnchantmentProbabilityNoticeItem(TypedDict):
    Name: str
    Count: int
    Value: str
    Memo: str
    Type: int

class EnchantmentProbabilityNotice(TypedDict):
    Name: str
    Items: List[EnchantmentProbabilityNoticeItem]
    Des: str
    Url: str
    API: str

class EnchantmentSerial(TypedDict):
    Name: str
    Des: str
    Url: str
    API: str

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

class EnchantmentAttribute(TypedDict):
    Category: EnchantmentCategory
    Range: EnchantmentRange

class EnchantableAttributeProbability(TypedDict):
    Attribute: EnchantmentAttribute
    Probability: float
    Row: EnchantmentRow
    Serial: EnchantmentSerial
