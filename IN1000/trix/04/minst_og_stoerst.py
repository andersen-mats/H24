liste = [6, -4, 7, -2, 8, -3, 9, -11]

minste = liste[0]
for n in liste:
    if n < minste:
        minste = n
print(minste)

stoerste = liste[0]
for n in liste:
    if n > stoerste:
        stoerste = n
print(stoerste)
