from .constants import *
from typing import Union, Callable
import requests
import datetime
import pandas as pd

tdf: Callable[[dict], pd.DataFrame] = lambda j: pd.DataFrame(data=j)


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
