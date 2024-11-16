def format_tekst(tekst, fil, maks):
    tekst = tekst.split()
    cnt = 1
    for ord in tekst:
        if cnt == maks:
            ord += "\n"
            cnt = 0
        else:
            ord += " "
        cnt += 1
        fil.write(ord)


def main():
    f = open("format.txt", "w")
    n = int(input("Maks antall ord pr. linje:\n> "))
    inp = input("Skriv en tekst:\n> ").strip()
    
    format_tekst(inp, f, n)
    
    f.close()


if __name__ == "__main__":
    main()
