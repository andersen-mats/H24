class Hund:
    def __init__(self, alder, rase):
        self._alder = alder
        self._rase = rase

    def hentRase(self):
        return self._rase

    def settAlder(self, alder):
        self._alder = alder

    def hentAlder(self):
        return self._alder

# Hva skrives ut?

# a) 
print(Hund(10, "Puddel").hentRase())

# `Puddel` skrives ut

# b)
print(Hund(12, "Labrador").hentAlder())

# `12` skrives ut

# c)  
litenValp = Hund(4, "Chihuahua")

litenValp.settAlder(10)
storValp = litenValp

storValp.settAlder(12)

print(litenValp.hentAlder())

# `12` skrives ut

#d)
litenValp = Hund(4, "Chihuahua")

litenValp.settAlder(10)
storValp = litenValp

storValp.settAlder(12)

litenValp = Hund(2, "Labrador")

print(storValp.hentRase())

# `Chihuahua` skrives ut
