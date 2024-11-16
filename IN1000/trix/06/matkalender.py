import random


def les_fil(filnavn):
    fil = open(filnavn, "r")
    retter = {}

    for linje in fil:
        rett, tid = map(str, linje.strip("\n").split(","))
        retter[rett] = tid
    fil.close()
    return retter


def velg(n, matretter):
    retter = list(matretter.keys())
    temp = []
    for _ in range(n):
        temp.append(retter[random.randint(0, len(retter) - 1)])
    return temp


def skriv_fil(filnavn, ordbok, liste):
    fil = open(filnavn, "w")
    for mat in liste:
        fil.write(f"Matrett: {mat}, tid: {ordbok[mat]}\n")
    fil.close()


matretter = les_fil("matretter.txt")
tilfeldig = velg(5, matretter)
skriv_fil("matplan.txt", matretter, tilfeldig)
