from .constants import *
from typing import Union
import requests
import datetime


def get(url: str = "") -> requests.Response: # Union[dict, str]:
    r = requests.get(url=url, headers={
        "Referer": f"{MAIN_URL}"
    })
    return r


def post(url: str, p) -> requests.Response:
    r = requests.post(url=url, headers={
        "Referer": f"{MAIN_URL}"
    }, data=p)
    return r


def checkSymbol(_sym: str = "") -> bool:
    try:
        r = post(f"{MAIN_URL}/api/tickers", {"symbol": _sym})
    except Exception as e:
        print(f"Exception (error: {e})")
        return False
    if r.status_code == 200: # // 100 == 2:
        return len([k for k in r.json() if k["ticker"] == str(_sym).upper()]) == 1
    return False

