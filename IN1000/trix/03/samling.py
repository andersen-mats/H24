# a) Ordene i en setning
# Jeg vil bruke dict, fordi da kan man lagre hvor i setningen ordet forekommer, samt
# hvor mange ganger det forekommer. Eksempel:

import re

def ord_funksjon(setning):

    setning = re.findall(r'\w+', setning)

    # {ord: [{pos: []}, {antall: n}]}

    ordbok = {}

    for i in range(len(setning)):
        ord = setning[i].lower()
        if ord in ordbok:
            ordbok[ord][0]["pos"].append(i)
            ordbok[ord][1]["antall"] += 1
        else:
            ordbok[ord] = [{"pos": [i]}, {"antall": 1}]

    return ordbok

inp = input()
print(ord_funksjon(inp))

# b) De latinske navnene paa alle de forskjellige spiselige soppene:
# Jeg gaar utifra at det finnes en slags konvensjon for arter og denslags.
# Jeg vill brukt en dict, med underarter og denslags. Da kan vi ogsaa noeste inn mer informasjon, som sesong, geografisk omraade, mm.
# Men det simpleste er nok en mengde, fordi vi ikke kan tillate duplikater, og fordi rekkefoelge ikke har noe aa si.

# c) Navnene paa alle klassekamerater ville vaert en liste, for den kan vi lett sortere med innebygde metoder.

# d) maaltid for hver dag, dict, hvor hver dag er en noekkel som tilsvarer et maaltid.

# e) for aa telle hvor mange arter jeg ser i hagen hver dag, etter art, ville jeg brukt en dict,
# hvor hver dag er noekkel. Saa kan vi noeste inn enda en dict, med artens navn, og hvor mange jeg saa.

# f) alle primtall under 1000, vi kunne brukt et set(). Rekkefoelgen er ikke viktig, og vi tillater ikke duplikater.
