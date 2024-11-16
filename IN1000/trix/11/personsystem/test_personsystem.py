from person import Person
from personsystem import Personsystem

def main():
    personsystem = Personsystem()
    navner = ["Said","Mats","Moumouh","Alice","Bob","Charlie","Ola"]
    for navn in navner:
        personsystem.legg_til(Person(navn))

    for navn in navner:
        assert personsystem.finn_person(navn) is not None


if __name__ == "__main__":
    main()
