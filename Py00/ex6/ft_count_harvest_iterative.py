def ft_count_harvest_iterative() -> None:
    total_days = int(input("Days until harvest: "))
    for day in range(1, total_days + 1):
        print("Day", day)
    print("Harvest time!")
