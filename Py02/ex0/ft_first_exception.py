def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


def main() -> None:
    print("=== Garden Temperature ===")
    print()
    user_input = input("Enter garden temperature: ")
    test_temperature(user_input)
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
