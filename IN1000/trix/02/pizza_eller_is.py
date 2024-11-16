def spoer_is():
    antall = int(input("Hvor mange is vil du ha?\n> "))
    print(f"Det blir {30 * antall} kr.")

def spoer_pizza():
    type = input("Hvilken pizza vil du ha?\n> ")

    if type == "ost":
        pris = 80
    else:
        pris = 100

    print(f"Du vil ha {type}. Det blir {pris} kr.")

def spoer_spise():
    spise = input("Hva vil du spise?\n> ")
    if spise == "is":
        spoer_is()
    elif spise == "pizza":
        spoer_pizza()
    else:
        print("Det har vi ikke.")

spoer_spise()
