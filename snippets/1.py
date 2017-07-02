from setuptools import find_packages, setup

setup(
    name='foo',
    version='0.0.1',
    packages=find_packages(exclude=["tests"]),
)
