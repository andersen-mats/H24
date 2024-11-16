MATRISE = [[0, 1, 2], [3, 2, 1], [1, 1, 0]]


def func(n, liste):
    ny = []
    for ele in liste:
        ele += n
        ny.append(ele)
    return ny

def foo(matrise):
    ny = []
    for n in range(len(matrise)):
        ny.append(func(n + 1, matrise[n]))

    return ny

for i in MATRISE:
    print(i)
print()
matrise = foo(MATRISE)

for i in matrise:
    print(i)

