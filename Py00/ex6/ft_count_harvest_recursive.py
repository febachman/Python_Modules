def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    print_days(days)
    print("Harvest time!")


def print_days(days: int) -> None:
    if days == 1:
        print("Day 1")
        return
    print_days(days - 1)
    print("Day", days)
