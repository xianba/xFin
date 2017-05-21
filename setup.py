#!/usr/bin/env python

from setuptools import setup

setup(name='xfin',
      version='1.0.0',
      packages=['xfin'],
      entry_points={
          'console_scripts': [
              'xfin = xfin.main:main'
          ]
      },
      )
