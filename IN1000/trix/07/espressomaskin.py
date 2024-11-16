class Espressomaskin:
    def __init__(self, kapasitet):
        self._kapasitet = kapasitet
        self._mengde = kapasitet
        print(f"Espressomaskinen har makskapasitet paa {self._kapasitet}")
    
    def lag_espresso(self):
        espresso_mengde = 40
        if self._mengde >= espresso_mengde:
            self._mengde -= espresso_mengde
            print(f"Lager espresso. Maskinen har naa {self._mengde}ml vann igjen")
        else:
            print("Ikke nok vann igjen til espresso")
            if input("vil du fylle paa mer vann? ") == "ja":
                self.fyll_vann(int(input("Hvor mye vann: ")))


    def lag_lungo(self):
        lungo_mengde = 110
        if self._mengde >= lungo_mengde:
            self._mengde -= lungo_mengde
            print(f"Lager lungo. Maskinen har naa {self._mengde}ml vann igjen")
        else:
            print("Ikke nok vann igjen til lungo.")
            if input("vil du fylle paa mer vann? ") == "ja":
                self.fyll_vann(int(input("Hvor mye vann: ")))

    def fyll_vann(self, ml):
        if self._mengde + ml >= self._kapasitet:
            print("Du har fylt opp maskinen.")
            self._mengde = self._kapasitet
        else:
            self._mengde += ml
            print(f"Du har fyll paa {ml}ml vann.")

    def hent_mengde(self):
        return self._mengde
