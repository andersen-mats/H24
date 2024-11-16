
# a) Skriv en funksjon equals() som tar inn to lister som argumenter og sjekker om 
# listene har de samme elementene i samme rekkefølge. Hvis ja, returneres True, 
# ellers False. Dette skal du gjøre med beslutninger og løkker.

# b) Utfordring Skriv en funksjon same_set() som også tar inn
# to lister som argumenter og sjekker om listene inneholder de 
# samme elementene i en tilfeldig rekkefølge uten å bruke innebygd funksjon set(). 
# Du trenger ikke å ta høyde for duplikater. For eksempel vil kall på funksjonen gitt listene under returnere True.

# [1, 4, 9, 16, 9, 7, 4, 9, 11]

# [11, 11, 7, 9, 16, 4, 1]

def equals(list1, list2):
    for i in range(len(list1)):
        if list1[i] != list2[i] or len(list1) != len(list2):
            return False
        else:
            return True


print(equals([3,2,1], [3,2,1]))


def same_set(list1, list2):
    cmp = []
    for element in list1:
        if element not in cmp:
            cmp.append(element)
    
    for element in list2:
        if element not in cmp:
            return False
    return True


print(same_set([1,2,3], [1,2,3,2,2,1]))


