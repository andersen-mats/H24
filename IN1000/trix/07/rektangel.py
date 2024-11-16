class Rektangel:
    def __init__(self, bredde, lengde):
        self._bredde = bredde
        self._lengde = lengde

    def __del__(self):
        print("Destructor paakalt")

    def info(self):
        return f"rektangelet har bredde {self._bredde} og lengde {self._lengde}"

    def oek_lengde(self, oekning):
        self._lengde += oekning

    def oek_bredde(self, oekning):
        self._bredde += oekning

    def areal(self):
        return self._bredde * self._lengde

    def omkrets(self):
        return self._bredde * 2 + self._lengde * 2
    
    def reduser(self, n):
        if n < self._lengde and n < self._bredde:
            self._lengde -= n
            self._bredde -= n
            print("Redusering gikk fint.")
        else:
            print(f"Kan ikke redusere objekt. {n} er for stort.")
