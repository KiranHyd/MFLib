from setuptools import setup, Extension, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="MFLib",
    version="2.9",
    author="KiranHyd",
    author_email="kiran.ksoft@gmail.com",
    description="Library for getting real time Mutual funds info",
    license="MIT",
    keywords="amfi, quote, mutual-funds, funds, bse, nse, market, stock, stocks",
    install_requires=['requests', 'bs4', 'httpx', 'pandas', 'yfinance'],
    url="https://github.com/KiranHyd/MFLib",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data={'': ['*.json']}
)
