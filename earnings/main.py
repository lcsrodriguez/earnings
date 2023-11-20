from .utils import *


## TODO: Calendar (with earnings calendar)

class Earnings:
    __slots__ = ("_sym", "stockData", "earningsDates", "dtInstance",)

    def __init__(self, sym: str = ""):
        self._sym = str(sym).upper()
        self.dtInstance: datetime.datetime = datetime.datetime.now().replace(microsecond=0)
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

    def getTicker(self) -> str:
        return self._sym

    def __eq__(self, other: object) -> bool:
        return self._sym == other._sym and self.dtInstance == other.dtInstance

    def getEarningsDates(self):
        if self.earningsDates["last"] is None or self.earningsDates["next"] is None:
            if self.stockData is None:
                self.getCompanyInfo(_full=False)
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

    def getCompanyInfo(self, _full: bool = True) -> dict:
        if self.stockData is None:
            r = get(f"{MAIN_URL}/api/getstocksdata/{self._sym}")
            self.stockData = r.json()
            if _full and "website" not in self.stockData:
                self.stockData["website"] = get(f"{MAIN_URL}/api/gotowebsite/{self._sym}").url
        return self.stockData

    def getQuotes(self) -> dict:
        r = get(f"{MAIN_URL}/api/getquotes/{self._sym}")
        return r.json()[self._sym]

    def getExpectedPriceAction(self) -> list:
        r = post(f"{MAIN_URL}/api/vote",
                 {
                     "ticker": self._sym,
                     "vote": DEFAULT_POST_OPTIONS["vote"]
                 })
        res = r.json()
        res[-1]["totalHolds"] -= 1
        return res

    def getExpectedPriceAction(self) -> list:
        r = post(f"{MAIN_URL}/api/expect",
                 {
                     "ticker": self._sym,
                     "vote": DEFAULT_POST_OPTIONS["expect"]
                 })
        res = r.json()
        res[-1]["meet"] -= 1
        res[-1]["total"] -= 1
        return res

    def getLastEarningsDetails(self) -> dict:
        r = get(f"{MAIN_URL}/api/epsdetails/{self._sym}")
        res = r.json()
        res["article"] = get(f"{MAIN_URL}/api/newsarticle/{self._sym}/{r.json()['fileName']}").json()
        return res

    def getChartData(self, freq: Frequency = Frequency.DAILY) -> dict:
        f_url: str = "weekly" if freq == Frequency.WEEKLY else ""
        r = get(f"{MAIN_URL}/api/get{f_url}chartdata/{self._sym}")
        return r.json()

    def getNews(self) -> dict:
        """
        Returning news articles (in time-descending order)
        :return:
        """
        r = get(f"{MAIN_URL}/api/getnews/{self._sym}")
        return r.json()

    def getArticle(self, articleId: int) -> dict:
        r = get(f"{MAIN_URL}/api/newsarticle/{self._sym}/{articleId}")
        return r.json()

    def getPivotPoints(self) -> dict:
        r = get(f"{MAIN_URL}/api/pivotpoints/{self._sym}/")
        return r.json()

    def getCandleCurrentQuarter(self) -> dict:
        r = get(f"{MAIN_URL}/api/getqhist/{self._sym}/")
        return r.json()

    def getWeeklyNetBuyRating(self) -> dict:
        r = get(f"{MAIN_URL}/api/anrechist?symbol={self._sym}")
        return r.json()
