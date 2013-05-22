#!/usr/bin/env python

from os.path import abspath, dirname, join
from setuptools import setup, find_packages
from sys import path

path.append(abspath(join(dirname(__file__), 'src')))

from glast import __VERSION__


def read(fname):
    return open(join(dirname(__file__), fname)).read()
# Installation Dependencies
install_dependencies = [
    'gunicorn == 0.17.4',
    'pyserial == 2.6',
    'RPi.GPIO == 0.5.2a',
    'Flask == 0.9',
]

setup(
    name='lapsr',
    version=__VERSION__,
    author='Eric George',
    description='',
    long_description=read('README.rst'),
    zip_safe=False,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=install_dependencies,
    include_package_data=True,
    classifiers=[
        'Environment :: Console',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
