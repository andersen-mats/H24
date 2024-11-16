from film import Film

def test_film():
    # __init__
    print("Oppretter to filmer")
    film1 = Film("film1", 2001)
    film2 = Film("film2", 2002)
    print()
    # hent_tittel
    print("Skriver ut titler på to filmer")
    print(film1.hent_tittel())
    print(film2.hent_tittel())
    print()

    # ny_skuespiller
    print("Legger til to skuespillere")
    film1.ny_skuespiller("Ola Nordmann", "John Smith")
    film1.ny_skuespiller("Kari Bjerke", "Alice in Wonderland")
    print("Har lagt til Ola Nordmann som `John Smith`")
    print("og Kari Bjerke som `Alice in Wonderland` til `film1`")
    print()

    print("Tester ulovlig innlegging av skuespiller")
    film1.ny_skuespiller("Ola Nordmann", "John Applesauce")
    film1.ny_skuespiller("Kari Bjerke", "Alice Crypto")
    print()
    
    print(f"{film1.hent_tittel()} har skuespillerne {film1.hent_skuespiller_navn()}")
    print()
    # skriv_ut_film
    print("Skriver ut all info om to filmer:")
    film1.skriv_ut_film()
    film2.skriv_ut_film()
    print()
    
    # hent_alle_skuespiller_navn
    print("Henter og skriver ut alle skuespillernavn for en film:")
    for skuespiller in film1.hent_skuespiller_navn():
        print(skuespiller)
    print()

    # sjekk_periode
    print ("Sjekker at en film er i oppgitt periode")
    print(film1.sjekk_periode(2000, 2005))

    # Sjekk om en film er i en periode som skal gi False
    print ("Sjekker at en film ikke kan være produsert før og etter samme år")
    print(film1.sjekk_periode(2001, 2001))

    # sjekk_tittel
    print("Sjekker om starten på en films tittel kjennes igjen")
    print(film1.sjekk_tittel(""))
    print(film1.sjekk_tittel("fil"))
    print(film1.sjekk_tittel("film1"))
    print(film1.sjekk_tittel("film10"))
    print() 

    # __str__
    print("Skriver ut en film med print (test av __str__)")
    print(film1)
    print()

    
    # test __eq__ (frivillig)
    # film3 har samme tittel og aar som film1
    film3 = Film("film1", 2001)
    print("tester __eq__ med to ulike filmer:")
    print(film1 == film2)
    print("\nTester __eq__ med to like filmer:")
    print(film1 == film3)


test_film()
