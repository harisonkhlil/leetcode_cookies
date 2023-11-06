#!/usr/bin/env python3

from setuptools import setup

setup(
    name="my_cookies",
    version="0.1",
    description="Get LeetCode cookies from browser",
    author="Harisonkhlil",
    author_email="harisonkhlil@gmail.com",
    keywords=["browser", "cookies"],
    packages=["my_cookies"],
    scripts=["bin/my_cookies"],
    install_requires=["browser_cookie3"],
)
