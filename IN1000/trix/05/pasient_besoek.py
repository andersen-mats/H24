def maks_besoek(liste):
    
    maks = 0

    for i in range(len(liste)):
        if len(liste[i]) > maks:
            maks = i + 1

    return maks

def faerrest_besoek(liste):

    minst = 999

    for i in range(len(liste)):
        if len(liste[i]) < minst:
            minste = i + 1

    return minste

def alle_besoek(liste):
    total = 0
    for i in range(len(liste)):
        total += len(liste[i])
    return total


def hvem_var_paa_dato(liste, dato):
    hvem = []
    for i in range(len(liste)):
        for n in liste[i]:
            if n == dato: 
                hvem.append(i + 1)

    return hvem

dato = 29
liste = [[4, 6, 1], [3, 4, 5, 7, 8, 9], []]
print(maks_besoek(liste))
print(faerrest_besoek(liste))
print(alle_besoek(liste)) 
print(hvem_var_paa_dato(liste, dato))

