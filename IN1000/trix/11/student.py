class Student:

    def __init__(self, navn, brukernavn, tlf):

        self._navn = navn
        self._brukernavn = brukernavn
        self._tlf = tlf

    def __str__(self):
        return f"Navn: {self._navn}\nBrukernavn: {self._brukernavn}\nTlf: {self._tlf}"

