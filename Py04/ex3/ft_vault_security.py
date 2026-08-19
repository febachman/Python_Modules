#!/usr/bin/env python3

import sys
import typing


def secure_archive(
    filename: str, mode: str = "r", content: str = ""
) -> typing.Tuple[bool, str]:
    try:
        if mode == "r":
            with open(filename, "r") as file:
                file_content = file.read()
                return (True, file_content)
        elif mode == "w":
            with open(filename, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
        else:
            return (False, f"Invalid mode: '{mode}'")
    except Exception as e:
        return (False, str(e))


def main() -> None:
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        mode = sys.argv[2] if len(sys.argv) > 2 else "r"
        content = sys.argv[3] if len(sys.argv) > 3 else ""
        success, result = secure_archive(filename, mode, content)
        print((success, result))
    else:
        print("=== Cyber Archives Security ===\n")
        print("Using 'secure_archive' to read from a nonexistent file:")
        print(secure_archive("/not/existing/file"))
        print("\nUsing 'secure_archive' to read from an inaccessible file:")
        print(secure_archive("/etc/master.passwd"))
        print("\nUsing 'secure_archive' to read from a regular file:")
        print(secure_archive("ancient_fragment.txt"))
        print(
            "\nUsing 'secure_archive' to write previous"
            "content to a new file:"
        )
        fragment_content = (
            "[FRAGMENT 001] Digital preservation protocols established 2087\n"
            "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
            "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
        )
        print(
            secure_archive
            ("secured_fragment.txt", mode="w", content=fragment_content)
        )


if __name__ == "__main__":
    main()
