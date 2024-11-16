class Person:

    def __init__(self, navn, adresse, postinfo, land, tlf, brukernavn):
        self._navn = navn
        self._adresse = adresse
        self._postinfo = postinfo
        self._land = land
        self._tlf = tlf
        self._brukernavn = brukernavn

    def hent_info(self):
        return f"""navn: {self._navn}
adresse: {self._adresse}
postinfo: {self._postinfo}
land: {self._land}
tlf: {self._tlf}
brukernavn: {self._brukernavn}"""

    def endre_navn(self, ny):
        self._navn = ny


