class Sau:
    def __init__(self, navn, posisjon):
        self._navn = navn
        self._posisjon = posisjon
        self._lever = True

    def blir_spist(self):
        self._lever = False

    def lever(self):
        return self._lever

    def hent_navn(self):
        return self._navn

    def hent_posisjon(self):
        return self._posisjon

