"""Run a Python script after preloading the local MSVC runtime DLLs.

The task-local virtual environment carries the runtime files needed by numba,
but Windows does not load them automatically from the environment root.
"""

import ctypes
import glob
import os
import runpy
import sys


venv_root = os.path.dirname(os.path.dirname(sys.executable))
for dll in glob.glob(os.path.join(venv_root, "*.dll")):
    ctypes.WinDLL(dll)

script = sys.argv.pop(1)
sys.argv[0] = script
sys.path.insert(0, os.path.dirname(os.path.abspath(script)))
if os.environ.get("FULLALPHA") == "1":
    import homo

    homo.ALPHA = "abcdefghijklmnopqrstuvwxyz"
runpy.run_path(script, run_name="__main__")
