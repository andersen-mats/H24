class Gruppe:
    def __init__(self, krav):
        self._krav = krav
        self._gruppe = []

    def legg_til_personer(personer):
        for person in personer:
            self._gruppe.append(person)

    def hent_personer():
        return self._gruppe

    def hent_krav():
        return self._krav

class Rom:
    def __init__(self, rom_nr, ant_senger, fasiliteter):
        self._rom_nr = rom_nr
        self._ant_senger = ant_senger
        self._fasiliteter = fasiliteter
        self._opptatt = False
        self._beboerer = []

    def __str__(self):
        return f"Rom nr: {self._rom_nr}\nAnt. senger: {self._ant_senger}\nFasiliteter: {' '.join[f for f in fasiliteter]}"
    
    def reserver(self, navn):
        if not self._opptatt:
            self._opptatt = True
            self._beboere = navn

    def hent_ant_senger(self):
        return self._ant_senger

    def passer(self, krav):
        for k in krav:
            if k not in self._fasiliteter:
                return False
        return True

    
            

        
    
