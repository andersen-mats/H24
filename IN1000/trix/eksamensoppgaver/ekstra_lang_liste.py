
def ekstra_lang(liste):
    ny_liste = list()

    cnt = 0
    while len(ny_liste) < len(liste) * 2:
        ny_liste.append(liste[cnt])
        ny_liste.append(42)
        cnt += 1

    return ny_liste

liste = ["Suppe", 8, "krabbeklo"]
print(ekstra_lang(liste))
