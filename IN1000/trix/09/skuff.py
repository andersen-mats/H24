from sokk import Sokk

class Skuff:
    def __init__(self):
        self._sokke_liste = list()
    def sett_inn_sokk(self, sokk):
        assert isinstance(sokk, Sokk)
        self._sokke_liste.append(sokk)
    def sjekk_status(self):
        self._venstre = 0
        self._hoyre = 0
        for sokk in self._sokke_liste:
            if sokk.hent_side() == "H":
                self._hoyre += 1
            else:
                self._venstre += 1
        if self._venstre == self._hoyre:
            print("Alt i orden")
            return
        print("Antallet stemmer ikke")
        return
