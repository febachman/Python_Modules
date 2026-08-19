#!/usr/bin/env python3

import sys
import typing


def display_archive_content(filename: str) -> None:
    print(f"Accessing file '{filename}'")
    try:
        file: typing.IO[str] = open(filename, "r")
        try:
            content = file.read()
            print("---")
            print()
            print(content)
            print()
            print("---")
            print(f"File '{filename}' closed.")
        finally:
            file.close()
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    display_archive_content(filename)


if __name__ == "__main__":
    main()
