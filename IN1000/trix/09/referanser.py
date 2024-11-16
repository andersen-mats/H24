# a)
def gjenta(a):
    a = a + a
    return a

a = "ab"
b = gjenta(a)
print(a+b)

# `ababab` skrives ut 

# b)

def voks(alder): 
    alder = alder+1

alder_1 = 20
voks(alder_1)
print(alder_1)

# `20` skrives ut

# c)

class Klasse:
    def __init__(self, a):
        self._a = a

    def pluss(self, b):
        a = self._a
        a += b
        return a

k = Klasse(5)
k.pluss(3)
print(k._a)

# `5` skrives ut 
