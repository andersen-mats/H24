skattekart = []

def skriv_ut(kart):
    
    # Print y-axis numbering
    y = [i for i in range(1, len(skattekart) + 1)]
    y = [str(i) for i in y]
    print(f"  {' '.join(y)}")

    for i in range(len(skattekart)):
        # print x-axis numbering 
        print(f"{i + 1} ", end="")
        # print the map
        print(" ".join(skattekart[i]))


def main():
    n = int(input("Hvor stort er karter? "))

    for i in range(n):
        rad = []

        for e in range(n):
            rad.append("O")

        skattekart.append(rad)

    skriv_ut(skattekart)
    
    print("Hvor skal du gjemme skatten?")
    
    while True:
        try:
            loc_x = int(input("x: "))
            loc_y = int(input("y: "))
            if loc_x not in range(1, n + 1) or loc_y not in range(1, n + 1):
                print("Skriv gyldig lokasjon!")
                raise ValueError
            else:
                break
        except:
            pass

    skattekart[loc_y - 1][loc_x - 1] = "X"
    skriv_ut(skattekart)
    skattekart[loc_y - 1][loc_x - 1] = "O"
    
    for i in range(15):
        print()

    print("Neste spiller sin tur!\nFinn skatten!\n")

    count = 0
    while True:

        skriv_ut(skattekart)

        while True:
            try:
                x = int(input("x: "))
                y = int(input("y: "))
                if x not in range(1, n + 1) or y not in range(1, n + 1):
                    print("Skriv gyldig lokasjon!")
                    raise ValueError
                else:
                    break
            except:
                continue

        if x == loc_x and y == loc_y:
            print("Spiller 2 fant skatten!!!\n")
            count += 1
            break
        else:
            skattekart[y - 1][x - 1] = "#"
            count += 1
            if count == 3:
                print("\nSpiller 1 vinner!\n")
                break

    skattekart[loc_y - 1][loc_x - 1] = "X"
    skriv_ut(skattekart)
    print(f"\nDet ble gjort {count} forsoek.\n")


if __name__ == "__main__":
    main()
