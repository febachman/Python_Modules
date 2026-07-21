class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(
            f"{self.name.capitalize()}: {self.height:.1f}cm, "
            f"{self.age} days old"
        )


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

    def produce_shade(self):
        print(
            f"Tree {self.name.capitalize()} now produces a shade of "
            f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, amount):
        self.height += amount

    def aging(self, days):
        self.age += days
        self.nutritional_value += days

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {round(self.nutritional_value)}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("rose", 15, 10, "red")
    rose.show()
    print(f"[asking the {rose.name} to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak = Tree("oak", 200, 365, 5)
    oak.show()
    print(f"[asking the {oak.name} to produce shade]")
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato = Vegetable("tomato", 5, 10, "april")
    tomato.show()
    print(f"[make {tomato.name} grow and age for 20 days]")
    tomato.grow(42)
    tomato.aging(20)
    tomato.show()
