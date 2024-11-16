import math

class Punkt:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def __str__(self):
        return f"x: {self._x}, y: {self._y}, z: {self._z}"

    def avstand(self, annen):
        return math.sqrt((annen._x - self._x) ** 2 + (annen._y - self._y) ** 2 + (annen._z - self._z) ** 2)

    def closest(self, liste):
        
        for i in range(len(liste)):
            if i == 0:
                foo = self.avstand(liste[i])
                bar = liste[i]
            if self.avstand(liste[i]) < foo:
                foo = self.avstand(liste[i])
                bar = liste[i]

        return bar
            
