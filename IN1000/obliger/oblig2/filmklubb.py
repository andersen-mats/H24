from film import Film

class Filmklubb:
    def __init__(self):
        self._filmer = []

    def les_filmer_fra_fil(self, filnavn):
        fil = open(filnavn, "r")
        
        for linje in fil:
            linje = linje.strip("\n").split(";")
            self._filmer.append(Film(linje[0], linje[1]))

        fil.close()

    def skriv_ut_alle_filmer(self):
        for film in self._filmer:
            film.skriv_ut_film()
            
    def registrer_film(self):
        navn = input("Legg til film: (tittel):\n> ").strip()
        aar = int(input("Utgivelsesaar:\n> "))
        filmen = Film(navn, aar)
        for film in self._filmer:
            if filmen == film:
                print("Filmen er allerede registrert")
                return 1
        self._filmer.append(filmen)

    def finn_film_tittel(self, tittel):
        for film in self._filmer:
            obj = film.hent_tittel()
            if tittel == "":
                return film
            if len(tittel) <= len(obj) and obj.startswith(tittel):
                return film

        return None

    def legg_til_skuespillere(self, film):
        while True:
            splr = input("Skuespiller: (`q` for aa slutte)\n> ").strip().title()
            if splr == "Q":
                break
            rolle = input("Rolle: (`q` for aa slutte)\n> ").strip().title()
            if rolle == "Q":
                break
            film.ny_skuespiller(splr, rolle)
    
    def finn_filmer_periode(self, aar1, aar2):
        matcher = []
        for film in self._filmer:
            if film.sjekk_periode(aar1, aar2):
                matcher.append(film)
        return matcher
