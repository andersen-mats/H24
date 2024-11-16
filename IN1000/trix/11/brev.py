class Brev:

    def __init__(self, avsender, mottaker):
        self._avsender = avsender
        self._mottaker = mottaker

    def skriv_linje(self, streng):
        self._innhold = streng

    def les_brev(self):
        print(f"Hei, {self._mottaker}!\n{self._innhold}\nHilsen fra\n{self._avsender}")

