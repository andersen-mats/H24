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

    def ledig(self):
        return not self._opptatt


class Hotell:

    def __init__(self, navn):
        self._navn = navn
        self._rom = dict()
        
        fil = file.open(navn, "r")

        for linje in fil:
            linje = linje.strip("\n").split()
            nr = linje.pop(0)
            senger = linje.pop(0) 
            krav = linje
            self._rom[nr] = Rom(nr, senger, krav)

        fil.close()

    def reserver(self, nr, gjester):
        self._rom[nr].reserver(gjester)

    def finn(krav):
        ret = []
        for nr in self._rom:
            if self._rom[nr].passer(krav):
                ret.append(self._rom[nr])
        return ret

class System:

    def __init__(self, hotellnavn):
        self._hoteller = dict()
        for n in hotellnavn:
            self._hoteller[n] = Hotell(n)

    def reserver(self, hotellnavn, romnr, gjester):
        if hotellnavn in self._hoteller:
            hotell = self._hoteller[hotellnavn]
            hotell.reserver(romnr, gjester)
        else:
            pass

    def _finn_passende(self, krav):
        ret = dict()

        for n in self._hoteller:
            hotell = self._hoteller[n]
            pot = hotell.finn(krav)
            for rom in pot:
                if rom.ledig():
                    if n in ret:
                        ret[n].append(rom)
                    else:
                        ret[n] = [rom]
        return ret

    def grupperes(self, gruppe):
        antpers = len(gruppe.hent_personer())
        har_rom = dict()
        for person in gruppe.hent_personer():
            har_rom[person] = False

        krav = gruppe.hent_krav()
        passer = this._finn_passende(krav)
        if not passer:
            print("ingen passende rom")
            return

        info = []
        
        for hotellnavn in passer:
            romliste = passer[hotellnavn]
            for rom in romliste:
                romplass = rom.hent_ant_senger()
                bosammen = []
                for _ in range(romplass):
                    if gruppe.hent_personer():
                        temp = gruppe.hent_personer().pop(0)
                        bosammen.append(temp)
                        har_rom[temp] = True
                info.append(f"Hotellnavn: {hotellnavn}, Rom: {str(rom)}")
                rom.reserver(bosammen)


        harikke = 0
        for person in har_rom:
            if not har_rom[person]:
                harikke += 1

        if harikke > 0:
            print(f"{harikke} personer har ikke faatt rom")
            return
        else:
            return info
