from foo import VERSION

major, minor, incremental = VERSION

if (major, minor) == ("3", "7"):
    workaround()
