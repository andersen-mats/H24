def vanlig_konkat(list1, list2):
    list3 = list1 + list2
    return list3

l1 = ["a", "b", "c"]
l2 = [1, 2, 3]

def annenhver_konkat(list1, list2):

    list3 = []

    for i in range(len(list1)):
        list3.append(list1[i])
        list3.append(list2[i])
    
    return list3

def tall_til_liste(n):
    list1 = []
    n = str(n)
    for c in n:
        list1.append(int(c))

    return list1


print(vanlig_konkat(l1, l2))
print(annenhver_konkat(l1,l2))
print(tall_til_liste(532))
