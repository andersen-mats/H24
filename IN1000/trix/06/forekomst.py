def les_tall_fra_fil(filnavn):
    liste = list()
    fil = open(filnavn, "r")
    for linje in fil:
        liste.append(int(linje.strip("\n")))
    return liste

def antall_forekomster(liste, n):
    cnt = 0
    for e in liste:
        if e == n:
            cnt += 1
    return cnt

def flest_forekomster(liste):
    freq = {}
    for e in liste:
        if not e in freq:
            freq[e] = 1
        else:
            freq[e] += 1
    temp = 0
    for e in freq:
        if freq[e] > temp:
            temp = freq[e]
            number = e

    return number

liste = les_tall_fra_fil("tall.txt")
print(antall_forekomster(liste, 2))
print(flest_forekomster(liste))
