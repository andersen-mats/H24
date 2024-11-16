import re

def legge():

    beholding = dict()
    stopword = "slutt"
    pattern = r"\d"

    while True:
        try:
            groennsak = input("Groennsak:\n> ")
            if groennsak == stopword:
                return beholding
            if re.search(pattern, groennsak):
                raise TypeError
        except TypeError:
            print("Skriv en gyldig groennsak.\n")
            continue

        while True:
            try:
                pris = input(f"Prisen til {groennsak}:\n> ")
                if pris == stopword:
                    return beholding
                int(pris)
            except ValueError:
                print("Oppgi gyldig tall")
                continue

            beholding[groennsak] = pris
            break
        
def main():
    beholding = legge()
    for groennsak in beholding:
        print(f"Groennssak: {groennsak}, pris: {beholding[groennsak]}")
    return 0

if __name__ == "__main__":
    main()
