class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.set_height(height, silent=True)
        self.set_age(age, silent=True)

    def get_height(self):
        return self._height

    def set_height(self, value, silent=False):
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            if not hasattr(self, '_height'):
                self._height = 0.0
        else:
            self._height = float(value)
            if not silent:
                print(f"Height updated: {int(self._height)}cm")

    def get_age(self):
        return self._age

    def set_age(self, value, silent=False):
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            if not hasattr(self, '_age'):
                self._age = 0.0
        else:
            self._age = float(value)
            if not silent:
                print(f"Age updated: {int(self._age)} days")

    def show(self, prefix=""):
        print(
            f"{prefix}: {self.name}: {self._height:.1f}cm, "
            f"{int(self._age)} days old"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    rose.show(prefix="Plant created: ")
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    rose.set_age(-10)
    print()
    rose.show(prefix="Current state: ")
