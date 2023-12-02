# `earnings` Python package

<img src="https://img.shields.io/static/v1?label=Languages&message=Python&color=ff0000"/>&nbsp;<img src="https://img.shields.io/static/v1?label=Restriction&message=NO&color=26c601"/> ![GitHub release (latest by date)](https://img.shields.io/github/v/release/lcsrodriguez/earnings) ![python version | 3.10+](https://img.shields.io/badge/Python%20version-3.10+-magenta) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![](https://img.shields.io/badge/Dependabot-enabled-blue)


## Overview

**`earnings`** is a Python package tailored to retrieve insightful earnings details, allowing users to collect previous and future earnings calendars, filter by US-equity ticker, define a custom portfolio, 

**DISCLAIMER**: *Data are provided as is. No warranty on data quality and accuracy. Please do your own research*

- [Overview](#overview)
- [Getting started](#getting-started)
- [Roadmap](#roadmap)
- [Project architecture](#project-architecture)
- [License](#license)

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
3. Execute the script:
```shell
python3 example.py
```

**Source**
1. Clone the repository from GitHub:
```
git clone https://github.com/lcsrodriguez/earnings.git
cd earnings
```

## Roadmap

See [ROADMAP.md](ROADMAP.md) file.

## Project architecture

```
.
├── LICENSE
├── README.md
├── earnings/
│   ├── __init__.py
│   ├── constants.py
│   ├── main.py
│   └── utils.py
├── examples/
│   └── main.py
├── out/
├── portfolios/
├── requirements.txt
└── setup.py
```

## License

**[Lucas RODRIGUEZ](https://lcsrodriguez.github.io)** (Maintainer & Developer)

[MIT](LICENSE)