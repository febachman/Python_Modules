class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = float(height) if height >= 0 else 0.0
        self._age = float(age) if age >= 0 else 0.0

    def get_height(self):
        return self._height

    def set_height(self, value):
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(value)
            print(f"Height updated: {int(self._height)}cm")

    def get_age(self):
        return self._age

    def set_age(self, value):
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = float(value)
            print(f"Age updated: {int(self._age)} days")

    def show(self):
        print(f"{self.name}: {self._height:.1f}cm, {int(self._age)} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    rose.set_age(-10)
    print()
    print("Current state: ", end="")
    rose.show()
