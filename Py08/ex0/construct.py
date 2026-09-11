#!/usr/bin/env python3

import sys
import os


def is_virtual_environment() -> bool:
    in_venv_env = "VIRTUAL_ENV" in os.environ
    in_venv_prefix = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    return in_venv_env or in_venv_prefix


def get_site_packages_path(venv_path: str) -> str:
    if os.name == 'nt':  # Windows
        return os.path.join(venv_path, "Lib", "site-packages")
    else:  # Unix / Linux / macOS
        py_version = f"python{sys.version_info.major}.{sys.version_info.minor}"
        return os.path.join(venv_path, "lib", py_version, "site-packages")


def handle_global_environment() -> None:
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print(r"matrix_env\Scripts\activate # On Windows")
    print("\nThen run this program again.")


def handle_virtual_environment() -> None:
    venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
    venv_name = os.path.basename(venv_path)
    site_packages = get_site_packages_path(venv_path)

    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("\nPackage installation path:")
    print(site_packages)


def main() -> None:
    if not is_virtual_environment():
        handle_global_environment()
    else:
        handle_virtual_environment()


if __name__ == "__main__":
    main()
