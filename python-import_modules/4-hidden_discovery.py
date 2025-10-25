#!/usr/bin/python3
import marshal
import types

def load_pyc(filename):
    with open(filename, "rb") as f:
        f.read(16)  # skip header for Python 3.7+ (magic number, timestamp, etc.)
        code = marshal.load(f)
    return types.ModuleType("hidden_4", type(code))

# Load the compiled module
import importlib.util
spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
hidden_4 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hidden_4)

# Print all names not starting with __
for name in sorted(name for name in dir(hidden_4) if not name.startswith("__")):
    print(name)
