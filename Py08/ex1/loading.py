#!/usr/bin/env python3

import sys
import importlib
from typing


REQUIRED_PACKAGES: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
    "requests": "Network access ready (Optional)",
}

def check_dependencies() -> None:
    """Check if all required packages are installed"""
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    
    missing_packages: list[str] = []
    
    for package, description in REQUIRED_PACKAGES.items():
        try:
            mod = importlib.import_module(package)
            version = getattr(mod, "__version__", "unknown")
            print(f"[OK] {package} ({version}) - {description}")
        except ImportError:
            print(f"[MISSING] {package} - Not installed")
            missing_packages.append(package)
    # Instead of letting Python crash with a ModuleNotFoundError,
    # importlib.import_module() dynamically tests if a package exists
    # in the current environment string-by-string. If it's installed,
    # getattr() safely extracts its version string (__version__).
    # If it fails, the except ImportError block catches the error cleanly
    # and tracks the missing item instead of halting execution immediately.

    if missing_packages:
        print("\nError: Missing required dependencies.")
        print("To install using pip:")
        print("  pip install -r requirements.txt")
        print("To install using Poetry:")
        print("  poetry install")
        sys.exit(1)

def main() -> None:
    check_dependencies()
    
    # Imports happen after verification
    import numpy as np  # type: ignore[import-untyped]
    import pandas as pd  # type: ignore[import-untyped]
    import matplotlib.pyplot as plt  # type: ignore[import-untyped]

    print("Analyzing Matrix data...")
    data = np.random.randn(1000, 2)
    df = pd.DataFrame(data, columns=["A", "B"])
    # This satisfies the requirement to avoid hardcoded lists or range().
    # np.random.randn(1000, 2) generates a 1,000-row by 2-column matrix
    # of floating-point numbers sampled from a standard normal distribution.
    # Wrapping it in pd.DataFrame turns that raw numerical array into a
    # structured table with labeled columns, ready for statistical analysis
    # using df.describe()

    print(df.describe())

if __name__ == "__main__":
    main()
