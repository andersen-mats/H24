class Blueberry:
    def __init__(self, size, berries):
        self._size = size
        self._berries = berries

    def water_plant(self):
        self._size += 3
        print("The plant has been watered.")

    def fertilize(self):
        self._berries += 5
        print("The plant has been fertilized.")

    def pluck(self, amount):
        self._berries -= amount
        if self._berries < 0:
            self._berries = 0
        print(f"{amount} berries was plucked from the tree.")

    def get_berries(self):
        return self._berries

    def get_berry_weight(self):
        return self._berries * 0.3

    def get_size(self):
        return self._size

berry1 = Blueberry(3, 5)
berry1.water_plant()
berry1.fertilize()
berry1.pluck(2)
print(berry1.get_berries())
print(berry1.get_berry_weight())
print(berry1.get_size())
