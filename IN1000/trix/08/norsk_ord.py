class NorskOrd:

    def __init__(self, ord):

        assert isinstance(ord, str)

        self._ord = ord

    def sjekk(self):

        tegn = ["æ", "ø", "å"]
        
        for c in tegn:
            if c in self._ord.lower():
                return True
        return False
    
    def skriv_ord(self):

        print(self._ord)
    
    def hent_ord(self):

        return self._ord

    def endre_ord(self, nytt):

        self._ord = nytt



    
