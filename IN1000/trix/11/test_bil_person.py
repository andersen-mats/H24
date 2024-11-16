from bil import Bil
from person import Person

def main():

    mercedes = Bil("svart", "Mercedes")
    toyota = Bil("gul", "Toyota")
    tesla = Bil("blaa", "Tesla")
    alice = Person("Alice")
    bob = Person("Bob")
    alice.kjop_bil(mercedes)
    alice.kjop_bil(toyota)
    alice.biler()
    bob.kjop_bil(tesla)
    bob.biler()

    alice.lei_bil(bob)
    alice.biler()
    bob.biler()
    alice.lei_bil(bob)
       


if __name__ == "__main__":
    main()
