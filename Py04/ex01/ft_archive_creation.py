#!/usr/bin/env python3

import sys
import typing


def display_archive_content(filename: str) -> typing.Optional[str]:
    print(f"Accessing file '{filename}'")
    content = ""
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
            print()
        finally:
            file.close()
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return None
    return content


def transform_and_save(content: str) -> None:
    print("Transform data:")
    lines = content.splitlines(keepends=True)
    transformed_lines = []
    for line in lines:
        if line.endswith("\n"):
            transformed_lines.append(line[:-1] + "#\n")
        else:
            transformed_lines.append(line + "#")
    transformed_content = "".join(transformed_lines)
    print("---")
    print()
    print(transformed_content)
    print()
    print("---")
    new_filename = input("Enter new file name (or empty): ")
    if new_filename == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_filename}'")
        try:
            new_file: typing.IO[str] = open(new_filename, "w")
            try:
                new_file.write(transformed_content)
                print(f"Data saved in file '{new_filename}'.")
            finally:
                new_file.close()
        except Exception as e:
            print(f"Error saving file '{new_filename}': {e}")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    content = display_archive_content(filename)
    if content is not None:
        transform_and_save(content)


if __name__ == "__main__":
    main()
