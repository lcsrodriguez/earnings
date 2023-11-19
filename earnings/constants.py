from enum import Enum
MAIN_URL: str = "https://www.earningswhispers.com"
DEFAULT_POST_OPTIONS: dict = {"expect": "Meet", "vote": "flat"}


class Frequency(Enum):
    DAILY: str = "daily"
    WEEKLY: str = "weekly"
