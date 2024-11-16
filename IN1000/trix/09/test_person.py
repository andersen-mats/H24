from person import Person

def main():

    mr = Person("Bob")
    mrs = Person("Alice")

    mr.status()
    mrs.status()

    mr.gifte(mrs)
    mrs.gifte(mr)

    mr.status()
    mrs.status()

if __name__ == "__main__":
    main()
