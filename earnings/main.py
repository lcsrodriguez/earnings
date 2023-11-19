from .utils import *


## TODO: Calendar (with earnings calendar)

class Earnings:
    __slots__ = ("_sym", "stockData")

    def __init__(self, sym: str = ""):
        self._sym = str(sym).upper()
        self.stockData: Union[dict, None] = None

    def _premCheck(self) -> bool:
        return checkSymbol(self._sym)

    def __str__(self) -> str:
        return f"Earnings ({self._sym})"

    def __repr__(self) -> None:
        print(self.__str__())

    def getCompanyInfo(self) -> dict:
        if self.stockData is None:
            r = get(f"{MAIN_URL}/api/getstocksdata/{self._sym}")
            self.stockData = r.json()[self._sym]
        return self.stockData

    def getExpectationsEstimates(self):
        ...

    def getQuotes(self):
        r = get(f"{MAIN_URL}/api/getquotes/{self._sym}")
        return r.json()[self._sym]

    def getExpectedPriceAction(self):
        r = post(f"{MAIN_URL}/api/vote",
                 {
                     "ticker": self._sym,
                     "vote": DEFAULT_POST_OPTIONS["vote"]
                 })
        r.json()[-1]["totalHolds"] -= 1
        return r.json()

    def getExpectedPriceAction(self):
        r = post(f"{MAIN_URL}/api/expect",
                 {
                     "ticker": self._sym,
                     "vote": DEFAULT_POST_OPTIONS["expect"]
                 })
        r.json()[-1]["meet"] -= 1
        r.json()[-1]["total"] -= 1
        return r.json()
