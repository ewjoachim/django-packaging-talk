about = {}
with open("foo/_version.py") as f:
    exec(f.read(), about)
# ...
setup(
    version=about["__version__"]
)
