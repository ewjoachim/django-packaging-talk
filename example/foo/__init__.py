import pkg_resources

from .real_stuff import main


__version__ = pkg_resources.get_distribution(__name__).version
VERSION = tuple(__version__.split("."))


if __name__ == '__main__':
    main()
