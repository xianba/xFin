#!/usr/bin/env python

from setuptools import setup
import codecs
import os

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

long_desc = """
xFin
===============

Target Users
--------------
* financial market analyst of China
* learners of financial data analysis with pandas/NumPy
* people who are interested in China financial data
Installation
--------------
    pip install xfin

Upgrade
---------------
    pip install xfin --upgrade
"""

setup(name='xfin',
      version='1.0.2',
      packages=['xfin'],
      long_description=long_desc,
      entry_points={
          'console_scripts': [
              'xfin = xfin.main:main'
          ]
      },
      )
