#!/usr/bin/env python
import os
from setuptools import setup, find_packages


def install():
    desc = 'A Python service to parse eshuushuu!'
    ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__)))

    with open(os.path.join(ROOT, 'README.md'), 'r') as r:
        long_description = r.read()

    setup(
        name='pyeshuushuu',
        version='0.1',
        description=desc,
        long_description=long_description,
        author='Lulu300 & Shorty',
        author_email='',
        url='https://github.com/Lulu300/pyeshuushuu',
        classifiers=['Operating System :: POSIX',
                     'Operating System :: Microsoft :: Windows',
                     'Operating System :: MacOS :: MacOS X',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 3.2',
                     'Programming Language :: Python :: 3.3',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'Programming Language :: Python :: 3.7',
                     'Programming Language :: Python :: 3 :: Only'
                     ],
        packages=find_packages(),
        install_requires=[
            'requests',
            'bs4',
            'click'
        ],
    )


if __name__ == "__main__":
    install()
