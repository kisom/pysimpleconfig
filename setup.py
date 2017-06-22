# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(name='simpleconfig',
      version='2.0',
      py_modules=['simpleconfig'],
      description='Dead simple configuration file parser.',
      long_description = readme,
      author='Kyle Isom',
      author_email='coder@kyleisom.net',
      license=license,
      url='http://kisom.github.com/pysimpleconfig',
)

