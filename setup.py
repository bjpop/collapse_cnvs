#!/usr/bin/env python

from distutils.core import setup

LONG_DESCRIPTION = \
'''The program'''

setup(
    name='collapse_cnvs',
    version='0.1.0.0',
    author='Bernie Pope',
    author_email='bjpope@unimelb.edu.au',
    packages=['collapse_cnvs'],
    package_dir={'collapse_cnvs': 'collapse_cnvs'},
    entry_points={
        'console_scripts': ['collapse_cnvs = collapse_cnvs.collapse_cnvs:main']
    },
    url='https://github.com/bjpop/collapse_cnvs',
    license='LICENSE',
    description=('A prototypical bioinformatics command line tool'),
    long_description=(LONG_DESCRIPTION),
    install_requires=["networkx"],
)
