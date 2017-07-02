from setuptools import find_packages, setup

setup(
    name='foo',
    version='0.0.1',
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    description='Foo, Bar Baz!',
    long_description='Foo, a deer, a female deer... '
                     'Bar a note to follow Foo... '
                     'Baz, a name, I call myself...',
    url='https://github.com/myself/foo/',
    author='My Self',
    author_email='foo@bar.com',  # *
)
