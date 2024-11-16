def nest(liste):
    
    for i in range(len(liste)):
        if i == 0:
            pass
        else:
            if liste[i] < liste[i - 1]:
                temp = liste[i]
                liste[i] = liste[i - 1]
                liste[i] = temp

    liste = set(liste)
    liste = list(liste)
    minste = liste[1] 
    return minste

print(nest([1,1,2,2,3,4,5]))
