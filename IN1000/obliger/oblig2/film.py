class Film:
    def __init__(self, tittel, aar):
        self._tittel = tittel
        self._aar = aar
        self._skuespillere = {}
    
    # returnerer en liten oversikt
    def __str__(self):
        return f"{self._tittel} ({self._aar})"

    # sjekker egt. bare om __str__ returnerer det samme paa begge
    def __eq__(self, other):
        if str(self) == str(other):
            return True
        return False

    def hent_tittel(self):
        return self._tittel
    
    def ny_skuespiller(self, navn, rolle):
        if navn in self._skuespillere:
            print(f"Skuespilleren `{navn}` finnes allerede")
            return 1
        self._skuespillere[navn] = rolle
    
    # returnerer liste av noekler i ordbok
    def hent_skuespiller_navn(self):
        return list(self._skuespillere.keys())
        
    # returnerer None
    def skriv_ut_film(self):
        print(f"{self._tittel} ({self._aar}) - Medvirkende:")
        for skuespiller in self._skuespillere:
            print(f"{skuespiller} som {self._skuespillere[skuespiller]}")

    # sjekker om den er mellom gitt periode
    def sjekk_periode(self, aar1, aar2):
        if int(self._aar) > int(aar1) and int(self._aar) < int(aar2):
            return True
        return False
    
    # tom streng gir alltid True
    def sjekk_tittel(self, tittel_start):
        if tittel_start == "":
            return True
        if len(tittel_start) > len(self._tittel):
            return False
        for i in range(len(tittel_start)):
            if tittel_start[i] != self._tittel[i]:
                return False
        return True
