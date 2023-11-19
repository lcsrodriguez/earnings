from .utils import *


## TODO: Calendar (with earnings calendar)

class Earnings:
    __slots__ = ("_sym", "stockData", "earningsDates")

    def __init__(self, sym: str = ""):
        self._sym = str(sym).upper()
        self.stockData: Union[dict, None] = None
        self.earningsDates: dict = {"last": None, "next": None}

    def _premCheck(self) -> bool:
        return checkSymbol(self._sym)

    def __str__(self) -> str:
        return f"Earnings ({self._sym})"

    def __repr__(self) -> None:
        print(self.__str__())

    def __hash__(self) -> int:
        return hash(self._sym)

    def getEarningsDates(self):
        if self.earningsDates["last"] is None or self.earningsDates["next"] is None:
            if self.stockData is None:
                self.getCompanyInfo()
            if "." not in self.stockData["lastEPSTime"]:
                self.stockData["lastEPSTime"] += ".00"
            if "." not in self.stockData["nextEPSDate"]:
                self.stockData["nextEPSDate"] += ".00"
            if "." not in self.stockData["confirmDate"]:
                self.stockData["confirmDate"] += ".00"
            self.earningsDates["last"] = {
                "event_dt": datetime.datetime.strptime(self.stockData["lastEPSTime"], '%Y-%m-%dT%H:%M:%S.%f')}
            self.earningsDates["next"] = {
                "event_dt": datetime.datetime.strptime(self.stockData["nextEPSDate"], '%Y-%m-%dT%H:%M:%S.%f'),
                "confirm_dt": datetime.datetime.strptime(self.stockData["confirmDate"], '%Y-%m-%dT%H:%M:%S.%f'),
                "release_counter": int(self.stockData["releaseTime"])
            }
        return self.earningsDates

    def getCompanyInfo(self) -> dict:
        if self.stockData is None:
            r = get(f"{MAIN_URL}/api/getstocksdata/{self._sym}")
            self.stockData = r.json()
            if "website" not in self.stockData:
                self.stockData["website"] = get(f"{MAIN_URL}/api/gotowebsite/{self._sym}").url
        return self.stockData

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
