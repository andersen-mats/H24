from side import Side

class Firkant:
    def __init__(self):
        self._sider = {
            "venstre": None,
            "hoyre": None,
            "oppe": None,
            "nede": None
        }

    def __str__(self):
        if self.er_fullstendig():
            temp = list(self._sider.values())
            temp2 = list(self._sider.values())
            temp2 = [x.hent_farge() for x in temp2]
            return f"omkrets: {sum([x.hent_lengde() for x in temp])}, farger: {' '.join(temp2)}"
        return "Firkanten er ikke fullstendig."

    def legg_til_side(self, side, plassering):
        assert isinstance(side, Side)
        assert plassering in self._sider
        if self._sider[plassering] is None:
            self._sider[plassering] = side

    def fjern_side(self, plassering):
        assert plassering in self._sider
        self._sider[plassering] = None

    def er_fullstendig(self):
        for side in self._sider:
            if self._sider[side] is None:
                return False
        return True
