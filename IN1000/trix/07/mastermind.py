from random import randint

class Mastermind:

    def __init__(self):
        self._code = []
        for n in range(4):
            n = randint(1,4)
            self._code.append(n)

    def get_inp(self):
        
        guess = []

        while True:
            inp = int(input("Your guess: "))
            if inp < 1111 or inp > 4444:
                print("Invalid guess. Only numbers from 1-4. Only use four numbers.")
                pass
            else:
                inp = str(inp)
                break

        for c in inp:
            guess.append(int(c))        
            self._guess = guess


    def check_guess(self):
        
        for i in range(len(self._guess)):
            if self._guess[i] == self._code[i]:
                self._guess[i] = "X"
        return self._guess

    def play(self):

        for i in range(10):
            self.get_inp()
            for n in self.check_guess():
                print(n, end="")
            print()
            if self._guess == ["X","X","X","X"]:
                print("YOU WIN.")
                break
            if i == 9:
                print("YOU LOSE.")


foo = Mastermind()
foo.play()
        
