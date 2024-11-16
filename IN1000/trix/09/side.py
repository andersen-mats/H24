class Side:
    def __init__(self, lengde, farge):
        assert isinstance(lengde, (int, float))
        assert isinstance(farge, str)
        self._lengde = lengde
        self._farge = farge

    def hent_lengde(self):
        return self._lengde

    def hent_farge(self):
        return self._farge
