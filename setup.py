import setuptools
from earnings import __version__

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="earnings",
    version=__version__,
    author="Lucas RODRIGUEZ",
    author_email="lcsrodriguez@pm.me",
    description=" Equity earnings Python package (confirmed calendar, news articles, earnings transcripts, ...)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
