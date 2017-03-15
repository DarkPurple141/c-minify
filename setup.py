#!/usr/bin/env python3

from setuptools import setup

setup(name='minifier',
      version='0.1',
      description='Minify a compilable C file. Project created for the purposes of' +
      'demoing bad style in C for my UNSW class.',
      url='https://github.com/DarkPurple141/c-minify',
      author='Alexander Hinds',
      author_email='alex.hinds141@gmail.com',
      license='MIT',
      packages=['minifier'],
      test_suite='tests',
      zip_safe=False)
