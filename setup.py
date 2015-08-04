# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 12:18:38 2015

@author: patrick
"""

from setuptools import setup, find_packages

setup( name = 'mpi',
      version = '0.1',
      description = 'Project to install and test mpi4py environment',
      author = 'Patrick Pisciuneri',
      author_email = 'phpisciuneri@gmail.com',
      packages = find_packages(),
      install_requires = [ 'mpi4py' ],
      zip_safe = False,
      test_suite = 'nose.collector',
      tests_require = [ 'nose' ]
      )