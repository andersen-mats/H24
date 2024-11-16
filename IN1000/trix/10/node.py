class Node:
    def __init__(self, nytt):
        self._innhold = nytt
        self._neste = None

    def ny_etterfolger(self, ny):
        self._neste = ny

    def hent_neste(self):
        return self._neste

    def hent_innhold(self):
        return self._innhold

