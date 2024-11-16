n = int(input("n: "))

teller = 0

while teller <= n:
    print(teller, end=" ")
    teller += 1
print("\nfin.\n")

while True:
    inp = input("Skriv noe: ")
    if inp != "slutt":
        print("hei")
    else:
        break
print("\nfin.\n")

while True:
    n = int(input("n: "))
    if n >= 10:
        break
