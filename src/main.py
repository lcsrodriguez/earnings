from .utils import *


class Earnings:
    __slots__ = ("sym",)

    def __init__(self, sym: str = ""):
        self.sym = sym

    def getCompanyInfo(self) -> dict:
        ...

    # 1: Expect -- 2: Vote

    def getExpectationsEstimates(self):
        ...