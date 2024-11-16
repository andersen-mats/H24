def arverekke(forfader, etterfolger, barn):

    rekke = []

    neste = forfader

    while neste in barn:
        rekke.append(neste)
        neste = barn[neste]
        if neste == etterfolger:
            rekke.append(neste)
            return rekke

    if neste == etterfolger:
        rekke.append(neste)
        return rekke

    return []

barn = {"Halfdan":"Harald", "Christian":"Hans", "Harald":"Eirik", "Eirik": "Torgrim", "Torgrim": "Jonas", "Hans": "Markus"}

print(arverekke("Halfdan", "Eirik", barn))
print(arverekke("Harald", "Jonas", barn))
print(arverekke("Christian", "Markus", barn))
