class Plant:
    def __init__(self, name, height, time, growth=0.0):
        self.name = name
        self.height = height
        self.time = time
        self.growth = growth

    def show(self):
        print(f"Created: {self.name}: {self.height:.1f}cm, {self.time} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
    garden = [rose, oak, cactus, sunflower, fern]
    for plant in garden:
        plant.show()

