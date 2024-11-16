class Sokk:
    def __init__(self, side):
        assert side.upper() == "H" or side == "V"
        self._side = side
    def hent_side(self):
        return self._side

