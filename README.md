<img src="/docs/MFLib.png"  height="150">

Python library for getting Mutual Funds data in India

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
[![Pypi](https://img.shields.io/badge/pypi-v2.9-green)](https://pypi.python.org/pypi/MFLib)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![License](https://img.shields.io/pypi/l/selenium-wire.svg)
[![Documentation](https://img.shields.io/badge/Documantation-latest-brightgreen)](https://MFLib.readthedocs.io/en/latest/)
[![Downloads](https://pepy.tech/badge/MFLib/month)](https://pepy.tech/project/MFLib)


Introduction
============
MFLib is a library for getting publically available Mutual Funds data in India. It can be used in various types of projects which requires getting live quotes for a given mutual fund scheme or build large data sets for further data analytics.

Features
=============

* Getting last updated quotes for Mutual fund scheme using scheme codes.
* Return data in Dataframe, json and dictionary formats.
* Getting quotes for all the schemes available with AMFI.
* Helper APIs to check whether a given Scheme code is correct.
* Getting all historical NAVs for a schemes.
* Getting list of all schemes with there Scheme codes.
* Get daily scheme performance.



<a href="https://buymeacoffee.com/kiranch" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="29" width="174">
</a>


---

# Development Instructions

## Running and Debugging

1. **Clone the repository and set up a virtual environment:**
	```bash
	git clone <your-repo-url>
	cd MFLib
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	```

2. **Run or debug in VS Code:**
	- Open the folder in VS Code.
	- Press `F5` or use the Run/Debug panel to start debugging.
	- Ensure the Python interpreter is set to your virtual environment (`venv`).

3. **Run tests (if available):**
	```bash
	python -m unittest discover tests
	```

## Building the Package

1. **Install build tools:**
	```bash
	pip install build
	```

2. **Build the package:**
	```bash
	python -m build
	```
	This will create `dist/` with `.tar.gz` and `.whl` files.

## Publishing to PyPI

1. **Install Twine:**
	```bash
	pip install twine
	```

2. **Upload to PyPI:**
	```bash
	twine upload dist/*
	```
	You will be prompted for your PyPI credentials.

---
