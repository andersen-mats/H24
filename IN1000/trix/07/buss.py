class Bus:
    def __init__(self, maxcap):
        self._maxcap = maxcap
        self._taken = 0
    
    def full(self):
        if self._taken == self._maxcap:
            return True
        else:
            return False

    def empty(self):
        if self._taken == 0:
            return True
        else:
            return False

    def enter(self, n):
        while not self.full() and n > 0: 
            self._taken += 1
            n -= 1
        if self.full():
            print("Bussen er full ...")

    def leave(self, n):
        while not self.empty() and n > 0:
            self._taken -= 1
            n -= 1
        if self.empty():
            print("Bussen er tom ...")

    def info(self):
        return self._taken
