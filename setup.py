#!/usr/bin/env python

from setuptools import setup

setup(name='finlib',
      version='1.0.0',
      packages=['finlib'],
      entry_points={
          'console_scripts': [
              'finlib = finlib.main:main'
          ]
      },
      )
