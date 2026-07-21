class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.stats = self.PlantStats()

    def grow(self, amount):
        self.height += amount
        self.stats.grow_count += 1

    def aging(self, days):
        self.age += days
        self.stats.age_count += 1

    class PlantStats:
        def __init__(self):
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def display(self):
            print(
                f"Stats: {self.grow_count} grow, "
                f"{self.age_count} age, {self.show_count} show"
            )

    @staticmethod
    def is_older_than_year(days):
        return days > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def show(self):
        self.stats.show_count += 1
        print(
            f"{self.name.capitalize()}: "
            f"{self.height:.1f}cm, {self.age} days old"
        )


def print_stats(plant):
    print(f"[statistics for {plant.name.capitalize()}]")
    plant.stats.display()
    if hasattr(plant.stats, "shade_count"):
        print(f" {plant.stats.shade_count} shade")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False

    def bloom(self):
        self.blooming = True

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if not self.blooming:
            print(f" {self.name.capitalize()} has not bloomed yet")
        else:
            print(f" {self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.stats.shade_count = 0

    def produce_shade(self):
        self.stats.shade_count += 1
        print(
            f"Tree {self.name.capitalize()} now produces a shade of "
            f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )
        print_stats(self)

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")
        print_stats(self)


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f" Seeds: {self.seeds}")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old ===")
    days_to_check = 30
    is_older = Plant.is_older_than_year(days_to_check)
    print(f"Is {days_to_check} days more than a year? -> {is_older}")
    days_to_check = 400
    is_older = Plant.is_older_than_year(days_to_check)
    print(f"Is {days_to_check} days more than a year? -> {is_older}")
    print()
    print("=== Flower")
    rose = Flower("rose", 15, 10, "red")
    rose.show()
    print_stats(rose)
    print(f"[asking the {rose.name} to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    print_stats(rose)
    print()
    print("=== Tree")
    oak = Tree("oak", 200, 365, 5)
    oak.show()
    print(f"[asking the {oak.name} to produce shade]")
    oak.produce_shade()
    print()
    print("=== Seed")
    sunflower = Seed("sunflower", 80, 45, "yellow")
    sunflower.show()
    print(f"[make {sunflower.name} grow, age and bloom]")
    sunflower.grow(30)
    sunflower.aging(20)
    sunflower.bloom()
    sunflower.show()
    print_stats(sunflower)
    print()
    print("=== Anonymous")
    Plant.anonymous().show()
    print_stats(Plant.anonymous())
