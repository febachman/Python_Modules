class Plant:
    def __init__(self, name, height, time, growth):
        self.name = name
        self.height = height
        self.time = time
        self.growth = growth

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.time} days old")

    def grow(self):
        self.height += self.growth

    def age(self):
        self.time += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25, 30, 0.8)
    rose.show()
    start_height = rose.height
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()
    total_growth = round(rose.height - start_height, 1)
    print(f"Growth this week: {total_growth}cm")
