#!/usr/bin/env python3
import pathlib

from setuptools import setup

import pluget

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pluGET",
    version=pluget.__version__,
    description="Powerful Package manager which updates plugins & server software for minecraft servers",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Neocky/pluGET",
    author="Neocky",
    author_email="Neocky@users.noreply.github.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=['pluget'],
    package_data={'pluget': ['pluget/*']},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "pluget=pluget.__init__:run",
        ]
    },
    install_requires=[
        'setuptools',
        'urllib3 ~= 1.21.1',
        'requests ~= 2.25.1',
        'paramiko ~= 2.7.2',
        'bcrypt ~= 3.2.0',
        'cryptography ~= 3.4.6',
        'pynacl ~= 1.4.0',
        'cffi ~= 1.14.5',
        'six ~= 1.15.0',
        'pycparser ~= 2.20',
        'pysftp ~= 0.2.9',
        'rich ~= 9.13.0',
        'commonmark ~= 0.9.1',
        'Pygments ~= 2.8.1',
        'typing_extensions ~= 3.7.4.3',
        'ruamel.yaml ~= 0.17.21',
    ]
)
