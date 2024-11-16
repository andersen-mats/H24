class Human:

    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._is_parent = False
        self._children = []

    def birthday(self):
        self._age += 1
        print(f"{self._name} turned {self._age} years old today.")

    def change_name(self, new):
        self._name = new

    def gets_child(self, child_name):
        child = Human(child_name, 0)
        self._children.append(child._name)
        if not self._is_parent:
            self._is_parents = True

    def get_name(self):
        return self._name

    def get_children(self):
        return self._children

    def get_age(self):
        return self._age

