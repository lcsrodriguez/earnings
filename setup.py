import setuptools
from earnings import __version__

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="earnings",
    version=__version__,
    author="Lucas RODRIGUEZ",
)
