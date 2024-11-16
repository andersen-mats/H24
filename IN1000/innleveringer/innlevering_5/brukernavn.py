# Denne funksjonen gjoer som dere ba om, men dersom veldig mange heter det samme,
# Saa vil den legge paa et tall
# Dessverre skiller ikke denne funksjonen mellom mellomnavn og etternavn
def lag_brukernavn(navn, ordbok):
    navn = navn.lower().split()
    brukernavn = navn[0]
    cnt1 = 0
    cnt2 = 0
    while True:
        if cnt1 != len(navn[1]):
            brukernavn += navn[1][cnt1]
            cnt1 += 1
        else:  
            if brukernavn + str(cnt2) not in ordbok:
                brukernavn += str(cnt2)
            else:
                cnt2 += 1
        if brukernavn not in ordbok:
            return brukernavn


def lag_epost(brukernavn, suffix):
    epost = brukernavn + "@" + suffix
    return epost


def skriv_ut_eposter(ordbok):
    for brukernavn in ordbok:
        epost = brukernavn + "@" + ordbok[brukernavn]
        print(epost)

# Her tester jeg med en liste som plassholder for ordboken
def test_funksjoner():
    ordbok = []
    b1 = lag_brukernavn("Kari Nordman", ordbok)
    assert b1 == "karin"
    ordbok.append(b1)

    b2 = lag_brukernavn("Ola Nordman", ordbok)
    assert b2 == "olan"
    ordbok.append(b2)

    b3 = lag_brukernavn("Mats Andersen", ordbok)
    assert b3 == "matsa"
    ordbok.append(b3)

    b4 = lag_brukernavn("Ola Nordman", ordbok)
    assert b4 == "olano"
    ordbok.append(b4)

    b5 = lag_brukernavn("O A", ordbok)
    assert b5 == "oa"
    ordbok.append(b5)

    b6 = lag_brukernavn("O A", ordbok)
    assert b6 == "oa0"
    ordbok.append(b6)

    b7 = lag_brukernavn("O A", ordbok)
    assert b7 == "oa1"
    ordbok.append(b7)

    b8 = lag_brukernavn("O A", ordbok)
    assert b8 == "oa2"
    ordbok.append(b8)

    assert lag_epost("karin", "uio.no") == "karin@uio.no"
    assert lag_epost("olan", "ifi.uio.no") == "olan@ifi.uio.no"
    assert lag_epost("matsa", "admin.uio.no") == "matsa@admin.uio.no"


def main():
    test_funksjoner()

    ordbok = {}

    while True:
        streng = input("Hva oensker du aa gjoere?")
        if streng == "i":
            navn = input("Navn: ")
            suffix = input("Epost-suffix: ")
            brukernavn = lag_brukernavn(navn, ordbok)
            ordbok[brukernavn] = suffix
        elif streng == "p":
            skriv_ut_eposter(ordbok)
        elif streng == "s":
            break
        else:
            print("`i` for aa lage epost\n`p` for aa skrive ut eposter\n`s` for aa slutte")


if __name__ == "__main__":
    main()
