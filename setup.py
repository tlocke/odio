from setuptools import setup

import versioneer
versioneer.VCS = 'git'
versioneer.versionfile_source = 'odio/_version.py'
versioneer.versionfile_build = 'odio/_version.py'
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = 'odio-'

cmdclass = dict(versioneer.get_cmdclass())

version = versioneer.get_version()

setup(
    name="odio",
    version=version,
    cmdclass=cmdclass,
    description="A library for the import / export of ODF documents.",
    author="Tony Locke",
    author_email="tlocke@tlocke.org.uk",
    url="https://github.com/tlocke/odio",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords="odf ods",
    packages=("odio", "odio.v1_1", "odio.v1_2"),
)
