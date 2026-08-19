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
            print("---\n")
            print(content)
            print("\n---")
            print(f"File '{filename}' closed.\n")
        finally:
            file.close()
    except Exception as e:
        print(
            f"[STDERR] Error opening file '{filename}': {e}",
            file=sys.stderr
        )
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
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename = sys.stdin.readline()
    if new_filename.endswith("\n"):
        new_filename = new_filename[:-1]

    if new_filename == "":
        print("Data not saved.")
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
            print(
                f"[STDERR] Error opening file '{new_filename}': {e}",
                file=sys.stderr
            )
            print("Data not saved.")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>", file=sys.stderr)
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    content = display_archive_content(filename)
    if content is not None:
        transform_and_save(content)


if __name__ == "__main__":
    main()
