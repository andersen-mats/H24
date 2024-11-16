class Person:
    def __init__(self, navn):
        self._navn = navn
    def hent_navn(self):
        return self._navn
