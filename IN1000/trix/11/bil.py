class Bil:
    def __init__(self, farge, merke):
        self._farge = farge
        self._merke = merke
        self._eier = None

    def __str__(self):
        return self._merke
    def eier(self, person):
        self._eier = person
