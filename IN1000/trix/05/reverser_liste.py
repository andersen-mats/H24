liste = ["en", "pluss", "to", "pluss", "tre", "er", "seks"]

def rev(liste):
    ny_liste = []

    for i in range(len(liste)):
        ny_liste.insert(0, liste[i])

    return ny_liste

print(rev(liste))
