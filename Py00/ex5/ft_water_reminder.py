def ft_water_reminder() -> None:
    water_count = int(input("Days since last watering: "))
    if water_count > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
