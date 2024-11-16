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

    # Her bruker jeg en annen metode enn i meny.py
    # Trikset er aa bruke noe som ble gjennomgaatt i forelesningen ...
    # Bare plis ignorer at jeg bruker ordboeker. I mitt forsvar stod det
    # Ingenting om at man ikke kunne bruke det; skjoent det impliseres
    # I oppgave 3.4.
    # Egentlig vil jeg bruke en mer automatisert og dermed kortere tilnaerming
    # enn if then if then if if if if,
    # men jeg skal bruke noe som ble gjennomgaatt i forelesningen naa
    # Uansett: prinsippet er det samme. Det var bare litt lettere for meg aa gjoere det saann.

    # Det er enten kjoett eller vegetar, derfor kan vi bruke `else`.
    # Vi trenger ikke a spesifisere `vegetar`, det ligger allerede implisitt
    if hovedretter[hovedrett_kunde] == "kjoett":
        if tilbehoer[tilbehoer_kunde] == "kjoett":
            print("Du spiser ikke nok groennsaker!")
        else:
            print(f"Du har valg {hovedrett_kunde} med {tilbehoer_kunde}")
    else:
        if tilbehoer[tilbehoer_kunde] == "vegetar":
            print("Du har valgt et vegetarmaaltid.")
        else:
            print(f"Du har valg {hovedrett_kunde} med {tilbehoer_kunde}")
 
    print("Maten kommer straks.")
    return 0


if __name__ == "__main__":
    main()
