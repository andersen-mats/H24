class Person:

    def __init__(self, navn):
        
        self._navn = navn
        self._gift = None

    def status(self):
        if self._gift is None:
            print(f"{self._navn} er singel.")
        else:
            print(f"{self._navn} er gift med {self._gift.hent_navn()}")

    def gifte(self, annen):
        
        self._gift = annen

    def hent_navn(self):
        
        return self._navn




