#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup
from setuptools import find_packages
from setuptools.command.install import install

from fancycmd import __version__


try:
    import readline
except ImportError:
    print("Err: readline not found")
    sys.exit(1)


def get_requirements():
    realpath = os.path.dirname(os.path.realpath(__file__))
    requirement_file = realpath + '/requirements.txt'
    requirements = []
    if os.path.isfile(requirement_file):
        with open(requirement_file) as f:
            requirements = f.read().splitlines()
    return requirements


def get_description():
    with open("README.md", "r") as f:
        description = f.read()

    return description


class UploadToPypi(install):
    """Upload the package to pypi. -- only for Maintainers."""

    def run(self):
        os.system("python setup.py bdist_wheel sdist")
        os.system("python setup.py sdist --format=bztar,zip upload")


class Install(install):
    """Configure and install the fancycmd package."""

    def run(self):
        if sys.platform.lower() not in ['cygwin', 'windows']:
            os.system("easy_install readline")

        install.run(self)


setup(
    name="fancycmd",
    version=__version__,
    author="Jeeva",
    author_email="hi@spidy.app",
    description="A fancy wrapper around readline",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/anyms/fancycmd",
    packages=find_packages(),
    keywords="cmd commandshell plugins",
    install_requires=get_requirements(),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: System :: Clustering",
        "Topic :: System :: Distributed Computing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Console"
    ],
    cmdclass={
        "pypi": UploadToPypi,
        "install": Install
    }
)