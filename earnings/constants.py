from enum import Enum

MAIN_URL: str = "https://www.earningswhispers.com"
DEFAULT_POST_OPTIONS: dict = {"expect": "Meet", "vote": "flat"}


class Frequency(Enum):
    DAILY: str = "daily"
    WEEKLY: str = "weekly"


class Sector(Enum):
    XLB: str = "Materials"
    XLC: str = "Communication Services"
    XLE: str = "Energy"
    XLF: str = "Financials"
    XLI: str = "Industrials"
    XLK: str = "Technology"
    XLP: str = "Consumer Staples"
    XLRE: str = "Real Estate"
    XLU: str = "Utilities"
    XLV: str = "Health Care"
    XLY: str = "Consumer Discretionary"
    ALL: int = -1


class Heatmap(Enum):
    PRICES_MOVES:       int = 0
    ESTIMATE_MOVES:     int = 1


class Output(Enum):
    DICT:               int = 0
    DATAFRAME:          int = 1
