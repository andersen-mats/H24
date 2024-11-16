def main():    
    maaneder = [
        "januar",
        "februar",
        "mars",
        "april",
        "mai",
        "juni",
        "juli",
        "august",
        "september",
        "oktober",
        "november",
        "desember",
    ]

    nr = int(input("Skriv tallet:\n> ")) - 1

    if nr in range(12):
        print(maaneder[nr])
    else:
        print("Ikke gyldig tall.")
if __name__ == "__main__":
    main()
