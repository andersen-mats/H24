def lengde(streng):
    cnt = 0
    for c in streng:
        cnt += 1
    return cnt


print(lengde("hei"))


def tell(streng, b):
    cnt = 0
    for c in streng:
        if c == b:
            cnt += 1
    return cnt


print(tell("hoho", "h"))


def tell_del(streng, delstreng):

    temp = list(delstreng)
    match = 0
    cnt = 0
    for i in range(len(streng)):
        if streng[i] == temp[0]:
            temp.pop(0)
            cnt += 1
            if cnt == len(delstreng):
                match += 1
                temp = list(delstreng)
                cnt = 0
    return match

print(tell_del("heheiheihhei", "hei"))


def range_liste(n, z):
    liste = list()
    while n < z:
        liste.append(n)
        n += 1
    return liste

print(range_liste(1, 10))
