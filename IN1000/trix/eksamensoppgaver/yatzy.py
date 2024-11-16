def er_hus(liste):
    temp = {}
    for n in liste:
        if n in temp:
            temp[n] += 1
        else:
            temp[n] = 1
    if set(temp.values()) == {3, 2}:
        return True

    return False

print(er_hus([5,5,5,6,6]))
print(er_hus([5,5,5,5,6]))

