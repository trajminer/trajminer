# Contribute

Everyone is welcome to contribute to the project, either by fixing [open issues](https://github.com/trajminer/trajminer/issues) or suggesting new features and reporting bugs (be sure your issue isn't already reported or even fixed).

### Important Links

- Issue tracker: https://github.com/trajminer/trajminer/issues
- Releases: https://pypi.org/project/trajminer
- Official wepbage: http://trajminer.github.io/

### Testing

	pytest trajminer

### Building the Docs

Inside the `doc` folder, run:

	bash build.sh [target-folder]

### Some Guidelines

Before submitting a pull request:
- Please check if your code follows the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide. You may do so by running `flake8`.
- Make sure you added the proper documentation (if adding new features) or corrected the existing one (if making changes to existing code). Also, ensure that you can build the docs.
- Please ensure that all tests are passing.
