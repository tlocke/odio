#!/usr/bin/env python

import versioneer
versioneer.VCS = 'git'
versioneer.versionfile_source = 'odio/_version.py'
versioneer.versionfile_build = 'odio/_version.py'
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = 'odio-'
from setuptools import setup

long_description = """\

Odio
----

A Python library for the input / output of ODF documents."""

cmdclass = dict(versioneer.get_cmdclass())

version = versioneer.get_version()

setup(
    name="odio",
    version=version,
    cmdclass=cmdclass,
    description="A library for the input / output of ODF documents",
    long_description=long_description,
    author="Tony Locke",
    author_email="tlocke@tlocke.org.uk",
    url="https://github.com/tlocke/odio",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
    keywords="odf ods",
    packages=("odio", "odio.v1_1", "odio.v1_2"),
    install_requires=['six'],
)
