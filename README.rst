.. -*- mode: rst -*-

Trajectory Mining Library
=========================

|CircleCI|_ |Release|_ |Python|_ |License|_ |CodeQuality|_

.. |CircleCI| image:: https://circleci.com/gh/trajminer/trajminer/tree/master.svg?style=svg
.. _CircleCI: https://circleci.com/gh/trajminer/trajminer/tree/master

.. |Release| image:: https://img.shields.io/pypi/v/trajminer.svg
.. _Release: https://pypi.org/project/trajminer

.. |Python| image:: https://img.shields.io/pypi/pyversions/trajminer.svg
.. _Python: https://pypi.org/project/trajminer

.. |License| image:: https://img.shields.io/pypi/l/trajminer.svg
.. _License: https://pypi.org/project/trajminer

.. |CodeQuality| image:: https://api.codacy.com/project/badge/Grade/18138918e47f407cabc4367f114492ce
.. _CodeQuality: https://www.codacy.com/app/trajminer/trajminer?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=trajminer/trajminer&amp;utm_campaign=Badge_Grade

Trajectory mining library inspired by and based on `scikit-learn <https://github.com/scikit-learn/scikit-learn>`_.

Installation
------------

To install trajminer using ``pip``, run: ::

	pip install trajminer

Trajminer requires **Python 3.6.5 or greater**, plus the following packages:
  - joblib >= 0.13.0
  - numpy >= 1.15.3
  - scikit-learn >= 0.19.1
  - keras >= 2.2.4
  - geohash2 >= 1.1
  - pandas >= 0.24.1

Documentation
-------------

The documentation of the latest version, as well as of past versions, can be found `here <https://trajminer.github.io/>`_.

Contribute
----------

Everyone is welcome to contribute to the project, either by fixing `open issues <https://github.com/trajminer/trajminer/issues>`_ or suggesting new features and reporting bugs (be sure your issue isn't already reported or even fixed).

Important Links
~~~~~~~~~~~~~~~

- `Issue tracker <https://github.com/trajminer/trajminer/issues>`_
- `Releases <https://pypi.org/project/trajminer>`_
- `Official wepbage <http://trajminer.github.io/>`_

Testing
~~~~~~~
::

  pytest trajminer

Checking Code Style (PEP8)
~~~~~~~~~~~~~~~~~~~~~~~~~~
::

	bash check_code_style.sh

Building the Docs
~~~~~~~~~~~~~~~~~

Inside the `doc` folder, run: ::

	bash build.sh [target-folder]

Some Guidelines
~~~~~~~~~~~~~~~

Before submitting a pull request:

- Please check if your code follows the `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ style guide. You may do so by running ``flake8``.
- Make sure you added the proper documentation (if adding new features) or corrected the existing one (if making changes to existing code). Also, ensure that you can build the docs.
- Please ensure that all tests are passing.

Citation in Scientific Works
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you use this library in any scientific work, please cite it as follows: ::

	@misc{petry2019trajminer,
	  title={Trajminer},
	  author={Petry, Lucas May and others},
	  year={2019},
	  howpublished={\url{https://trajminer.github.io}},
	}
