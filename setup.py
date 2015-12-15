#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='zomtems',
    packages=['zomtems'],
    version='0.1',
    description='Zommuting Items - Proving knowledge of secrets without revealing them',
    long_description=long_description,
    author='Tobias Kienzler',
    author_email='zommuter@gmail.com',
    url='https://github.com/zommuter/zomtems',
    license='GPL',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[],
)
