from menneske import Human

obj1 = Human("Ola Nordmann", 39)

print(obj1.get_name())
print(obj1.get_age())
print(obj1.get_children())

obj1.change_name("Ola Nordmann-Hansen")
obj1.birthday()
obj1.gets_child("Kari Nordmann-Hansen")
print(obj1.get_children())
