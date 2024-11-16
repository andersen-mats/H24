class Personsystem:

    def __init__(self):
        self._personer = []

    def legg_til(self, person):
        self._personer.append(person)

    def finn_person(self, navn):
        for person in self._personer:
            if navn == person.hent_navn():
                return person    
        return None


