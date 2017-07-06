from setuptools import setup

# everything is defined in setup.cfg
setup(
    entry_points={
        'console_scripts': ['foo=foo:main'],
    }
)
