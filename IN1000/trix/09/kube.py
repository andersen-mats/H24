class Kube:
    def __init__(self, lengde, bredde, dybde):
        self._lengde = lengde
        self._bredde = bredde
        self._dybde = dybde
    def __repr__(self):
        return f"lengde: {self._lengde}, bredde: {self._bredde}, dybde: {self._dybde}"

    def volum(self):
        return self._lengde * self._bredde * self._dybde

    def __gt__(self,other):
        return self.volum() > other.volum()
    def __int__(self):
        return self.volum()

    def __eq__(self, other):
        return self.volum() == other.volum()
