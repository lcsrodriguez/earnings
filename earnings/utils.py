from .constants import *
from typing import Union, Callable
import requests
import datetime
import pandas as pd
from functools import wraps

tdf: Callable[[dict], pd.DataFrame] = lambda j: pd.DataFrame(data=j)

gd: Callable[[Union[set, list]], dict] = lambda ks, d: {k: d[k] for k in list(ks) if k in d}


def get(url: str = "") -> requests.Response: # Union[dict, str]:
    r = requests.get(url=url, headers={
        "Referer": f"{MAIN_URL}"
    })
    return r


def post(url: str = "", p: Union[dict, None] = None) -> requests.Response:
    r = requests.post(url=url, headers={
        "Referer": f"{MAIN_URL}"
    }, data=p)
    return r
