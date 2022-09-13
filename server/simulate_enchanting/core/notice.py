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