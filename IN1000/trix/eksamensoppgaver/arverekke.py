def arverekke(forfader, etterkommer, barn):
    rekken = []

    temp = forfader

    while temp in barn:
        rekken.append(temp)
        if temp == etterkommer:
            return rekken
        temp = barn[temp]
    if temp == etterkommer:
        rekken.append(temp)
        return rekken
    return []

 # En stor ordbok med flere generasjoner
forstefodte = {
    "Odin": "Thor",
    "Thor": "Magni",
    "Magni": "Modi",
    "Modi": "Vidar",
    "Vidar": "Vali",
    "Vali": "Baldur",
    "Baldur": "Forseti",
    "Forseti": "Hermod",
    "Hermod": "Hodr",
    "Hodr": "Bragi",
    "Bragi": "Loki",
    "Loki": "Fenrir",
    "Fenrir": "Jormungandr",
    "Jormungandr": "Hel",
    "Hel": "Garm",
    "Garm": "Surtr",
    "Surtr": "Ymir",
    "Ymir": "Audumbla",
    "Audumbla": "Buri",
    "Buri": "Bor",
    "Bor": "Bestla",
}

