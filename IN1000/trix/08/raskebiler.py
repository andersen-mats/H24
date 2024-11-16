class Raskbil:
    def __init__(self, merke, bilnummer, navn, elbil):
        self._merke = merke
        self._bilnummer = bilnummer
        self._navn = navn
        assert isinstance(elbil, bool)
        self._elbil = elbil

    def skriv_info(self):
        print(f"merke: {self._merke}\nbilnummer: {self._bilnummber}\nnavn: {self.navn}")
        if self._elbil:
            print("type: elbil")
        else:
            print("type: bensin")
