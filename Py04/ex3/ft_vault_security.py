#!/usr/bin/env python3

def write_file(file_name: str, content: str | None) -> tuple[bool, str]:
    try:
        write_content = content if content is not None else ""
        with open(file_name, "w") as f:
            f.write(write_content)
        return True, "Content successfully written to file"
    except Exception as e:
        return False, str(e)


def read_file(file_name: str) -> tuple[bool, str]:
    try:
        with open(file_name, "r") as f:
            file_content = f.read()
        return True, file_content
    except Exception as e:
        return False, str(e)


def secure_archive(
    file_name: str,
    action: int | str = 1,
    content: str | None = None,
) -> tuple[bool, str]:
    try:
        if action == 2 or action == "write":
            return write_file(file_name, content)
        elif action == 1 or action == "read":
            return read_file(file_name)
        return False, "Error: Invalid action specified."
    except Exception as e:
        return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===")
    test_file = "test_vault.txt"

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    res1 = secure_archive("/not/existing/file", action=1)
    print(res1)

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    res2 = secure_archive("/etc/master.passwd", action=1)
    print(res2)

    test_file = "fragment_test.txt"
    sample_content = (
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
    )
    secure_archive(test_file, action="write", content=sample_content)

    print("\nUsing 'secure_archive' to read from a regular file:")
    res3 = secure_archive(test_file, action=1)
    print(res3)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    res4 = secure_archive("new_file.txt", action=2, content=sample_content)
    print(res4)


if __name__ == "__main__":
    main()
