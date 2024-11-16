def finn_butikk(handleliste, prisliste, butikker):
    total = 0
    for i in range(len(prisliste)):
        for vare in handleliste:
            total += prisliste[i][vare]
        if i == 0:
            butikk = i
            billigst = total
        elif total < billigst:
            butikk = i
            billigst = total
        total = 0
    return butikker[butikk]


prisliste = [
    {"salat" : 12, "fisk" : 99, "melk" : 12, "brod" :12},
    {"salat" : 22, "fisk" : 60, "melk" : 18, "brod" :21},
    {"salat" : 8, "fisk" : 120, "melk" : 10, "brod" :19},
    {"salat" : 18, "fisk" : 40, "melk" : 30, "brod" :59},
    {"salat" : 15, "fisk" : 200, "melk" : 40, "brod" :9},
]


butikker = ["Rema1000", "Meny", "Kiwi","Spar", "Joker"]
EKSEMPEL1 = ["salat", "melk"]
EKSEMPEL2 = ["fisk", "salat", "melk", "brod"]

print(finn_butikk(EKSEMPEL1, prisliste, butikker))
print(finn_butikk(EKSEMPEL2, prisliste, butikker))


