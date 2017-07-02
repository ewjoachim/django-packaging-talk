about = {}
with open("foo/about.py") as f:
    exec(f.read(), about)
# ...
setup(
    version=about["__version__"],
)
