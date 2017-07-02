package_name = 'foo'
about = {}
with open("foo/about.py") as f:
    exec(f.read(), about)
setup(
    name=package_name,
    version=about["__version__"],
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    description=about["__doc__"],
    long_description=open('README.md').read(),
    url=about["__url__"],
    author=about["__author__"],
    author_email=about["__author_email__"]
)
