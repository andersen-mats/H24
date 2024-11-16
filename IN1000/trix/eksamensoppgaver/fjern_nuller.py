def trim_zeros(liste):
    ny_liste = list()
    for i in range(len(liste)):
        liste[i] = str(liste[i])
    liste = "".join(liste)
    liste = liste.strip("0")
    for c in liste:
        ny_liste.append(int(c))
    return ny_liste



liste = [0,0,1,2,0,3,0,0,4,0,0,0,0,0,0,1,0,0,0,0,0]


print(trim_zeros(liste))


