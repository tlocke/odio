#!/usr/bin/env python

import versioneer
versioneer.VCS = 'git'
versioneer.versionfile_source = 'odfio/_version.py'
versioneer.versionfile_build = 'odfio/_version.py'
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = 'odfio-'
from setuptools import setup

long_description = """\

ODFIO
-----

A Python library for the input / output of
http://en.wikipedia.org/wiki/OpenDocument[ODF] documents."""

cmdclass = dict(versioneer.get_cmdclass())

version = versioneer.get_version()

setup(
    name="odfio",
    version=version,
    cmdclass=cmdclass,
    description="A library for the input / output of ODF documents",
    long_description=long_description,
    author="Tony Locke",
    author_email="tlocke@tlocke.org.uk",
    url="https://github.com/tlocke/odfio",
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
    packages=("odfio","odfio.v1_1"),
    install_requires=['six'],
)
