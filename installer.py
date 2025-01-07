# Check for and install the pytmx module

import os
import sys
import subprocess


def install(package):

    try:
        import package

    except ImportError:
        print(f"{package} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"{package} installed.")

    else:
        print(f"{package} found.")
