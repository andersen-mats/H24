class Trenode:

    def __init__(self, n):
        self._n = n
        self._hoyre = None
        self._venstre = None
        self._liste = []
    def hent_verdi(self):
        return self._n

    def har_venstre(self):
        if self._venstre is None:
            return False
        return True

    def har_hoyre(self):
        if self._hoyre is None:
            return False
        return True

    def utvid(self, x):
        barn = Trenode(x)
        temp = self.hent_verdi()
        if temp > x:
            # venstre
            if not self.har_venstre():
                self._venstre = barn
            else:
                self._venstre.utvid(x)
        elif temp < x:
            # hoyre
            if not self.har_hoyre():
                self._hoyre = barn
            else:
                self._hoyre.utvid(x)

    def skrivut(self):
        print(self.hent_verdi())
        if self.har_venstre():
            print("venstre")
            self._venstre.skrivut()
        if self.har_hoyre():
            print("hoyre")
            self._hoyre.skrivut()

    def sortert(self):
        self._liste.append(self.hent_verdi())
        if self.har_venstre():
            self._liste += self._venstre.sortert()
        if self.har_hoyre():
            self._liste += self._hoyre.sortert()

        return self._liste

    def finn(self, n):
        liste = self.sortert()
        if n in liste:
            return True
        return False

