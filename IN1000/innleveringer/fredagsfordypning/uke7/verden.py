from random import randint
from sau import Sau
from ulv import Ulv

class Verden:
    def __init__(self):
        self._sauer = []
        self._ulver = []

    def opprett_dyr(self, type, navn, posisjon):
        assert isinstance(type, str)
        if type.lower() == "sau":
            self._sauer.append(Sau(navn, posisjon))
        elif type.lower() == "ulv":
            self._ulver.append(Ulv(navn, posisjon)) 
        else:
            pass

    def beskriv(self):
        print("Sauer:")
        for sau in self._sauer:
            print(f"Navn: {sau.hent_navn()}\nPosisjon: {sau.hent_posisjon()}")
        print("Ulver:")
        for ulv in self._ulver:
            print(f"Navn: {ulv.hent_navn()}\nPosisjon: {ulv.hent_posisjon()}")

    def antall_sauer(self):
        return len([sau for sau in self._sauer if sau.lever()])

    def antall_ulver(self):
        return len(self._ulver)
    
    def oppdater(self):
        if randint(0,1) == 0:
            for ulv in self._ulver:
                ulv.beveg_hoeyre()
        else:
            for ulv in self._ulver:
                ulv.beveg_venstre()

        for ulv in self._ulver:
            for sau in self._sauer:
                if ulv.hent_posisjon() == sau.hent_posisjon() and sau.lever():
                    ulv.spis_sau(sau)
                    print(f"Ulven {ulv.hent_navn()} spiser sauen {sau.hent_navn()} paa posisjonen {ulv.hent_posisjon()}")

    def hent_feit_ulv(self):
        feitest = 0
        for ulv in self._ulver:
            vekten = ulv.hent_vekt()
            if vekten > feitest:
                feitest = ulv.hent_vekt()
                feitest_ulv = ulv
        return feitest_ulv

