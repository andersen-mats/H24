def les_bil(filnavn):
    resultatet = {}
    for line in filnavn:
        kol = line.strip("\n").split(":")
        resultatet[kol[0]] = kol[1]
    return resultatet

fil = open("bil.txt", "r")

bil = les_bil(fil)

for info in bil:
    print(f"{info}: {bil[info]}")

fil.close()
