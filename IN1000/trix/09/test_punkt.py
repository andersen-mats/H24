from punkt import Punkt

punkt1 = Punkt(1,1,1)
punkt2 = Punkt(5,5,6)
punkt3 = Punkt(1,20,1)
punkt4 = Punkt(4,6,1)

liste = [punkt2,punkt3,punkt4]

print(punkt1.closest(liste))
