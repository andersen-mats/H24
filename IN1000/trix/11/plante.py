class Plante:

    def __init__(self, maks):
        self._beholder = 0
        self._maks = maks
        self._levende = True

    def vann_plante(self, cl):
        self._beholder += cl
        if self._beholder > self._maks:
            self._levende = False

    def ny_dag(self):
        self._beholder -= 20
        if self._beholder <= 0:
            self._levende = False

    def levende(self):
        return self._levende



