from espressomaskin import Espressomaskin

obj1 = Espressomaskin(200)

obj1.lag_espresso()

obj1.lag_lungo()

obj1.fyll_vann(30)

print(obj1.hent_mengde())

obj1.lag_lungo()

print(obj1.hent_mengde())
