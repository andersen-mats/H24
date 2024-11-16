def stoerste(liste):
    tall1 = liste[0]
    tall2 = liste[0]

    for tall in liste:
        if tall > tall1:
            tall2 = tall1
            tall1 = tall
        elif tall > tall2:
            tall2 = tall

    return [tall1, tall2]

print(stoerste([1,2,3]))
