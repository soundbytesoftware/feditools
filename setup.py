#!/usr/bin/env python


from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    packages=find_packages(exclude=["test", "test.*"]),
    python_requires=">=3.7, <4",
    install_requires=[
        "urllib3==2.0.0a1",
    ],
    entry_points={
        "console_scripts": [
            "sample=sample:main",
        ],
    },
)
