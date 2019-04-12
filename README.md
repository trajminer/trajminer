# Trajectory Mining Library

| CircleCI      |
| ------------- |
| [![CircleCI](https://circleci.com/gh/trajminer/trajminer/tree/master.svg?style=svg)](https://circleci.com/gh/trajminer/trajminer/tree/master) |

Trajectory mining library inspired by and based on [scikit-learn](https://github.com/scikit-learn/scikit-learn).

## Installation

To install trajminer using `pip` run:

	pip install trajminer

Trajminer requires **Python 3.6.5 or greater**, plus the following packages:
- joblib >= 0.13.0
- numpy >= 1.15.3
- scikit-learn >= 0.19.1
- keras >= 2.2.4
- geohash2 >= 1.1
- pandas >= 0.24.1

## Documentation

The documentation of the latest version, as well as of past versions, can be found [here](https://trajminer.github.io/).

## Contribute

Everyone is welcome to contribute to the project, either by fixing [open issues](https://github.com/trajminer/trajminer/issues) or suggesting new features and reporting bugs (be sure your issue isn't already reported or even fixed).

### Important Links

- Issue tracker: https://github.com/trajminer/trajminer/issues
- Releases: https://pypi.org/project/trajminer
- Official wepbage: http://trajminer.github.io/

### Testing

	pytest trajminer

### Checking Code Style (PEP8)

	bash check_code_style.sh

### Building the Docs

Inside the `doc` folder, run:

	bash build.sh [target-folder]

### Some Guidelines

Before submitting a pull request:
- Please check if your code follows the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide. You may do so by running `flake8`.
- Make sure you added the proper documentation (if adding new features) or corrected the existing one (if making changes to existing code). Also, ensure that you can build the docs.
- Please ensure that all tests are passing.
