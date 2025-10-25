#!/usr/bin/env python3
from sys import argv

argc = len(argv) - 1  # number of arguments (excluding the script name)

if argc == 0:
    print("0 arguments.")
else:
    print("{} argument{}:".format(argc, "" if argc == 1 else "s"))
    for i in range(1, argc + 1):
        print("{}: {}".format(i, argv[i]))
