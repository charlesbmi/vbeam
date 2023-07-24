#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="vbeam",
    version="0.1.0",
    description="vbeam: a fast and differentiable beamformer",
    author="Magnus Dalen Kvalevåg",
    author_email="magnus.kvalevag@ntnu.no",
    url="https://bitbucket.org/ntnuultrasoundgroup/vbeam/src/main/",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pyuff_ustb",
        "scipy",
        "spekk",
    ],
)
