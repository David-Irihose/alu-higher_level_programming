#!/usr/bin/python3
if __name__ == "__main__":
    try:
        from variable_load_5 import a
    except ImportError:
        a = None

    if a is not None:
        print(a)
