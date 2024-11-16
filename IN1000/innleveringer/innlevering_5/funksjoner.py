# Enkelt program som summerer to tall og teller antall forekomster i streng

def adder(tall1, tall2):
    return (tall1 + tall2)

def tell_forekomst(streng, bokstav):
    freq = 0

    for c in streng:
        if c == bokstav:
            freq += 1
   
    return freq

print(adder(7, 8))
print(adder(2, 3))

streng = input("Gi meg en streng: ")
bokstav = input("Gi meg en bokstav: ")
freq = tell_forekomst(streng, bokstav)

print(f"{bokstav} forekommer {freq} ganger i {streng}")








