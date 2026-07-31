#!/usr/bin/env python3

import sys


def main():
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    total_args = len(sys.argv)
    if total_args == 1:
        print("No arguments provided!")
        print("Total arguments: 1")
    else:
        print(f"Arguments received: {total_args - 1}")
        for i in range(1, total_args):
            print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
