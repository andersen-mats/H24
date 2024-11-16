class Gjest:

    def __init__(self):
        self._verdi = 0

    def hent_verdi(self):
        return self._verdi

    def underhold(self, n):
        self._verdi += n
