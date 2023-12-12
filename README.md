# Earnings Python package

<img src="https://img.shields.io/static/v1?label=Languages&message=Python&color=ff0000"/>&nbsp;<img src="https://img.shields.io/static/v1?label=Restriction&message=NO&color=26c601"/> ![GitHub release (latest by date)](https://img.shields.io/github/v/release/lcsrodriguez/earnings) ![python version | 3.10+](https://img.shields.io/badge/Python%20version-3.10+-magenta) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 
![](https://img.shields.io/badge/Dependabot-enabled-blue)

![PyPI - Downloads](https://img.shields.io/pypi/dw/earnings)
![PyPI - Format](https://img.shields.io/pypi/format/earnings)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/earnings)
![PyPI - License](https://img.shields.io/pypi/l/earnings)
![PyPI - Version](https://img.shields.io/pypi/v/earnings)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/earnings)


## Overview

**`earnings`** is a lightweight and featureful Python package tailored to retrieve insightful earnings details, allowing users to collect previous and future earnings calendars, filter by US-equity ticker, define a custom portfolio and easily integrate reliable financial data into your applications.

**DISCLAIMER**: *Data are provided **AS IS** by external providers. No warranty on data quality and accuracy. Please do your own research* before deploying on production.

* [Overview](#overview)
* [Getting started](#getting-started)
* [Roadmap](#roadmap)
* [Project architecture](#project-architecture)
* [License & Credits](#license--credits)

## Getting started

**Package**:
1. Install package from official PyPi:
```shell
pip3 install earnings
```
2. Import package in your project code `example.py`:
```python
from earnings import *

def main(...) -> None:
    # Insert your logic

if __name__ == "__main__":
    main()
```
3. Execute the sample script:
```shell
python3 example.py
```

**Source**
1. Clone the repository from GitHub:
```shell
git clone https://github.com/lcsrodriguez/earnings.git
cd earnings/
```

2. Build virtual env and install dependencies
```shell
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```

## Roadmap

See [ROADMAP.md](docs/ROADMAP.md) file.

## Project architecture

```
./
├── AUTHORS
├── CITATION.cff
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── chver.sh
├── docs/
│   ├── README.md
│   └── ROADMAP.md
├── earnings/
│   ├── __init__.py
│   ├── constants.py
│   ├── main.py
│   └── utils.py
├── examples/
│   └── main.py
├── out/
├── portfolios/
│   └── template.pff
├── requirements.txt
└── setup.py
```

## License & Credits

- **[Lucas RODRIGUEZ](https://lcsrodriguez.github.io)** (Maintainer & Developer)

The [LICENSE](LICENSE) file contains the full license details.


If you are using this package for research purposes, you can quote it as shown below:

```shell
@software{RODRIGUEZ_PyEarnings_2023,
author = {RODRIGUEZ, Lucas},
month = dec,
title = {{earnings}},
url = {https://github.com/lcsrodriguez/earnings},
version = {1.1.0},
year = {2023}
}
```
