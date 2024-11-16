from person import Person

def lagre(person):
    fil = open("person.txt", "w")

    fil.write(person.hent_info())

    fil.close()

def les(filnavn):
    fil = open(filnavn, "r")
    linjer = []
    for linje in fil:
        linjer.append(linje)

    navn = linjer[0].split(":")[1].strip()
    adresse = linjer[1].split(":")[1].strip()
    postinfo = linjer[2].split(":")[1].strip()
    land = linjer[3].split(":")[1].strip()
    tlf = linjer[4].split(":")[1].strip()
    brukernavn = linjer[5].split(":")[1].strip()

    return Person(navn, adresse, postinfo, land, tlf, brukernavn)

ola = les("person.txt")

print(ola.hent_info())




