from student import Student

studenter = {
    "Alice": Student("Alice","Alice123", "123456789"),
    "Bob": Student("Bob","Bob123", "234567891"),
    "Charlie": Student("Charlie","Charlie123", "2345678912"),
}

for student in studenter:
    print(studenter[student])
    print()

def sjekk(studenter):
    while True:
        navn = input("Navn: ")
        if navn == "slutt":
            break
        if navn in studenter:
            print(studenter[navn])
        else: 
            print("Finnes ikke i systemet")

sjekk(studenter)
