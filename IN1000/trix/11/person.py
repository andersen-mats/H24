class Person:

    def __init__(self, navn):
        self._navn = navn
        self._mine_biler = []
        self._laante_biler = []

    def __str__(self):
        return f"{self._navn} sine biler: {' '.join([str(bil) for bil in self._mine_biler])}, laante biler: {' '.join([str(bil) for bil in self._laante_biler])}"
        
    def biler(self):
        print(self)

    def hent_mine_biler(self):
        return self._mine_biler

    def kjop_bil(self, bil):
        self._mine_biler.append(bil)
        bil.eier(self._navn)

    def lei_ut_bil(self):
        temp = self._mine_biler.pop(-1)
        return temp

    def lei_bil(self, utleier):
        if utleier.hent_mine_biler():
            self._laante_biler.append(utleier.lei_ut_bil())
            return True
        print("Utleieren har ingen biler tilgjengelig")
        return False

