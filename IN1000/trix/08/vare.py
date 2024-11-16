class Vare:
    def __init__(self, beskrivelse):
        self._beskrivelse = beskrivelse
        self._hoyestebud = None

    def by(self, bud):
        assert isinstance(bud, (int, float))
        
        if bud == 0:
            print("lureri")
            return

        if self._hoyestebud is None or bud > self._hoyestebud:
            self._hoyestebud = bud

    def se_bud(self):
        if self._hoyestebud is None:
            print("Ingen bud ennaa.")
            return None
        else:
            return self._hoyestebud


vare1 = Vare("TV")
print(vare1.se_bud())
vare1.by(0)
vare1.by(30)
print(vare1.se_bud())
vare1.by(31)
print(vare1.se_bud())

