from .utils import *


## TODO: Calendar (with earnings calendar)

class Earnings:
    __slots__ = ("_sym",)

    def __init__(self, sym: str = ""):
        self._sym = str(sym).upper()

    def _premCheck(self) -> bool:
        return checkSymbol(self._sym)

    def __str__(self) -> str:
        return f"Earnings ({self._sym})"

    def __repr__(self) -> None:
        print(self.__str__())

    def getCompanyInfo(self) -> dict:
        ...

    # 1: Expect -- 2: Vote

    def getExpectationsEstimates(self):
        ...

