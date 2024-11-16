def main():
    
    # Lager en dict/ordbok med varene og deres type
    hovedretter = {
        "biff": "kjoett",
        "lam": "kjoett",
        "salat": "vegetar",
        "margarita": "vegetar",
    }

    # Gjoer det samme for tilbehoeret
    tilbehoer = {
        "potet": "vegetar",
        "lammekraft": "kjoett",
        "chilisaus": "vegetar",
    }
    
    # Gaar igjennom hovedrettene, printer dem ut hver for seg
    print("hovedretter:")
    for rett in hovedretter:
        print(rett)

    # Printer ut et mellomrom, det ser litt penere ut
    print()
    
    # Gjoer det samme for tilbehoeret
    print("sideretter:")
    for ting in tilbehoer:
        print(ting)
    
    print()
    
    # Spoer bruker hvilken hovedrett de vil ha, sjekker om vi har det
    while True:
        hovedrett_kunde = input("Hvilken hovedrett oensker du?\n> ")
        if hovedrett_kunde not in hovedretter:
            print("Hva sa du?")
        else:
            break

    # Gjoer det samme for tilbehoeret
    while True:
        tilbehoer_kunde = input(f"Hvilket tilbehoer vil du ha?\n> ")
        if tilbehoer_kunde not in tilbehoer:
            print("Hva sa du?")
        else:
            break

    # Hvis x og x saa A, hvis y og y saa B, hvis x og y eller y og x, saa C
    if hovedretter[hovedrett_kunde] == "kjoett" and tilbehoer[tilbehoer_kunde] != "vegetar":
        print("Du spiser ikke nok groennsaker!!!!")
    elif hovedretter[hovedrett_kunde] == "vegetar" and tilbehoer[tilbehoer_kunde] == "vegetar":
        print("Du har valgt et vegetarmaaltid.")
    else:
        print(f"Du har valgt {hovedrett_kunde} med {tilbehoer_kunde}")

    print("Maten kommer straks.")
    return 0


if __name__ == "__main__":
    main()
