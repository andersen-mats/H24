def addisjon(tall1,tall2):
    return tall1 + tall2


def subtraksjon(tall1,tall2):
    return tall1 - tall2


def divisjon(tall1,tall2):
    return tall1 / tall2


def tommer_til_cm(tommer):
    assert tommer > 0
    return tommer * 2.54


def beregning():
    n = float(input("n: "))
    m = float(input("m: "))

    print(f"{n} + {m} = {addisjon(n,m)}")
    print(f"{n} - {m} = {subtraksjon(n,m)}")
    print(f"{n} / {m} = {divisjon(n,m)}")

    tommer = float(input("Tommer: "))

    print(f"{tommer} er {tommer_til_cm(tommer)} cm")


tall1 = 1
tall2 = 1
print(f"{tall1} + {tall2} = {addisjon(2,2)}")

tester = {2:3,3:5,1:7,6:2}

for test in tester:
    n = test
    m = tester[test]

    assert addisjon(n,m) == n + m
    assert subtraksjon(n,m) == n - m
    assert divisjon(n,m) == n / m

beregning()

