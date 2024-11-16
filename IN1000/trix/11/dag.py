class Dag:

    def __init__(self, dato, nedbor):
        self._dato = dato
        self._nedbor = nedbor
    
    def __str__(self):
        return f"{self._dato}: {self._nedbor} mm nedbor"

    def hent_dato(self):
        return self._dato

    def hent_nedbor(self):
        return self._nedbor


