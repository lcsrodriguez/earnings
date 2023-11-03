from .constants import *
from typing import Union
import requests


def get(url: str = "") -> requests.Response: # Union[dict, str]:
    r = requests.get(url=url, headers={
        "Referer": "https://www.earningswhispers.com"
    })
    return r


def post(url: str, p) -> requests.Response:
    r = requests.post(url=url, headers={
        "Referer": "https://www.earningswhispers.com"
    }, data=p)
    return r


def checkSymbol(_sym: str = "") -> bool:
    try:
        r = post("https://www.earningswhispers.com/api/tickers", {"symbol": _sym})
    except Exception as e:
        print(f"Exception (error: {e})")
        return False
    if r.status_code == 200: # // 100 == 2:
        return len([k for k in r.json() if k["ticker"] == str(_sym).upper()]) == 1
    return False

