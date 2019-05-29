#!/usr/bin/env python

from setuptools import setup

setup(name='xfin',
      version='1.0.2',
      packages=['xfin'],
      long_description = open("README.md").read(),
      long_description_content_type="text/markdown",
      entry_points={
          'console_scripts': [
              'xfin = xfin.main:main'
          ]
      },
      )
