def opprett_filen():

    f = open("test.in", "w")
    linjer = [i for i in range(10)]
    for n in linjer:
        f.write(str(n) + "\n")
    f.close()


def skriv_ut_foerste_linjer(filnavn, antall_linjer):
    
    f = open(filnavn, "r")
    cnt = 0
    for line in f:
        if cnt == antall_linjer:
            break
        print(line.strip("\n"))
        cnt += 1

def skriv_ut_siste_linjer(filnavn, antall_linjer):

    f = open(filnavn, "r")
    elements = list()
    for line in f:
        elements.append(line.strip("\n"))
    for element in range(antall_linjer, len(elements)):
        print(element)
    f.close()

def main():

    n = 5

    opprett_filen()
    skriv_ut_foerste_linjer("test.in", n)
    print()
    skriv_ut_siste_linjer("test.in", n)

if __name__ == "__main__":
    main()
