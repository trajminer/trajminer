from setuptools import setup, find_packages
from os import path


JOBLIB_MIN_VERSION = '0.13.0'
NUMPY_MIN_VERSION = '1.15.3'
SKLEARN_MIN_VERSION = '0.19.1'
KERAS_MIN_VERSION = '2.2.4'
GEOHASH2_MIN_VERSION = '1.1'
PANDAS_MIN_VERSION = '0.24.1'

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='trajminer',
    version='0.1.0.a2',
    description='A trajectory mining library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://trajminer.github.io/',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License'
    ],
    keywords='trajectory mining',
    packages=find_packages(exclude=['contrib', 'doc', 'tests']),
    install_requires=[
        'joblib>={0}'.format(JOBLIB_MIN_VERSION),
        'numpy>={0}'.format(NUMPY_MIN_VERSION),
        'scikit-learn>={0}'.format(SKLEARN_MIN_VERSION),
        'keras>={0}'.format(KERAS_MIN_VERSION),
        'geohash2>={0}'.format(GEOHASH2_MIN_VERSION),
        'pandas>={0}'.format(PANDAS_MIN_VERSION)
    ]
)
