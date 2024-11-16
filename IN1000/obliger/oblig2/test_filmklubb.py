from film import Film
from filmklubb import Filmklubb

def testprogram():

    # __init__
    print("oppretter Filmklubb-objekt")
    filmklubb = Filmklubb()

    # les_filmer_fra_fil
    print("Leser filmer fra fil")
    filmklubb.les_filmer_fra_fil("filmer.txt")
    print()

    # skriv_ut_alle_filmer
    filmklubb.skriv_ut_alle_filmer()
    print()

    # registrer_film
    print("Registrerer ny film")
    filmklubb.registrer_film()
    print()
    filmklubb.skriv_ut_alle_filmer()
    print()
    
    # Hvis _eq_ er implementert i Film og testes i registrer_film:
    print("Prøver å registrere film som allerede finnes")
    filmklubb.registrer_film()
    print()

    # finn_film_tittel
    print("Leter etter film med (start på) usannsynlig tittel")
    print(filmklubb.finn_film_tittel("xyz"))
    print()

    print("Leter etter film med (start på) tittel 'Hidden '")
    # Kall på metoden med argument "Hidden "
    print(filmklubb.finn_film_tittel("Hidden "))
    print()

    # legg_til_skuespillere
    print("Legg til skuespillere for en film" )
    filmtest = filmklubb.finn_film_tittel("Hidden ")
    filmklubb.legg_til_skuespillere(filmtest)
    print()
    filmklubb.skriv_ut_alle_filmer()
    print()

    # finn_film_periode
    # Kall på metoden med argumentene etter=2000 og før=2024
    print("Leter ett filmer produsert etter 2000 og før 2024:")
    liste = filmklubb.finn_filmer_periode(2000,2024)
    for film in liste:
        print(film.hent_tittel())
    print()

    # Kall på finn_film_periode med argumentene etter=2020 og før=2020
    print("Leter etter filmer produsert etter 2020 og før 2020:")
    liste2 = filmklubb.finn_filmer_periode(2020,2020)
    print(liste2)
testprogram()
