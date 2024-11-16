class Rorbu:

    def __init__(self):
        self._gjester = []

    def legg_til_gjest(self, ny):
        for gjest in self._gjester:
            gjest.underhold(1)
        self._gjester.append(ny)

    def fortell_vits(self, n):
        for gjest in self._gjester:
            gjest.underhold(n)
    
    def hent_gjester(self):
        return len(self._gjester)

    def morsomt(self):
        avg = 0

        for gjest in self._gjester:
            avg += gjest.hent_verdi()

        avg = avg / len(self._gjester)
        if avg < 200:
            print("Kjedelig kveld")
        elif avg < 400:
            print("Dette var litt goey")
        elif avg < 600:
            print("Dette var artig")
        else:
            print("Helt ekstremt artig")
