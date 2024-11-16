class Bilde:
    def __init__(self, hoyde, bredde, salgspris):
        self._hoeyde = hoyde
        self._bredde = bredde
        self._salgspris = salgspris

    def hentForhold(self):
        sideforhold = self._bredde / self._hoeyde
        return sideforhold

    def hentSalgspris(self):
        return self._salgspris


# Er denne koden gyldig, og hva skrives isaafall ut?
# Ja, den er gyldig.
# a) 1.5 skrives ut
# b) 2000 skrives ut 
# c) 5001.0 skrives ut 
# d) feilmelding 
# e) feilmelding
# f) 4500



