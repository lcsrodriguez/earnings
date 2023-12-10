import setuptools
from earnings import __version__

with open("README.md", "r") as f:
    long_description = f.read()

PYTHON_MODULE_NAME: str = "earnings"
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setuptools.setup(
    name=PYTHON_MODULE_NAME,
    py_modules=[PYTHON_MODULE_NAME],
    version=__version__,
    author="Lucas RODRIGUEZ",
    author_email="lcsrodriguez@pm.me",
    license="MIT",
    url="https://github.com/lcsrodriguez/earnings",
    description="Equity earnings Python package (confirmed calendar, news articles, earnings transcripts, ...)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'': '.'},
    install_requires=REQUIREMENTS,  # [],
    python_requires='>=3.10',
)
