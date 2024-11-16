class Fruit:
    def __init__(self, name, water, eat):
        self.name = name
        self.water = water
        self.eat = eat
        
        assert isinstance(self.name, str)
        assert isinstance(self.water, (int, float)) or self.water == None
        assert isinstance(self.eat, (bool)) or self.eat == None
        if isinstance(self.water, (float, int)):
            assert self.water > 0

    def get_name(self):
        return self.name
    def get_water(self):
        return self.water
    def get_eat(self):
        return self.eat

