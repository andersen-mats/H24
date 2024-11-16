def main():

    penger = 0

    try:
        antall = int(input("Hvor mange hoener bor paa garden? "))
    except:
        print("Ugydldig antall.")
        return 1

    while antall > 0:

        rev_inp = input("Kommer reven? (ja/nei) ").lower()

        if rev_inp == "ja":
            rev = True
        elif rev_inp == "nei":
            rev = False
        else:
            print("Ugyldig svar.")
            return 2

        bonde_inp = input("Sover bonden? (ja/nei) ").lower()

        if bonde_inp == "ja":
            bonde = False
        elif bonde_inp == "nei":
            bonde = True
        else:
            print("Ugyldig svar.")
            return 3

        
        if rev and not bonde:
            antall -= 3
            if antall >= 0:
                print(f"Reven kom. Tre hoener ble spist. Det er naa {antall} hoener igjen")
            else:
                print(f"Reven kom. Tre hoener ble spist. Det er naa ingen hoener igjen.")
        elif rev and bonde:
            penger += 190
            print(f"Reven kom. Bonden tok den. Han tjente 190kr, og har naa {penger}kr")
        else:
            pass

    print(f"GAME OVER. Bonden har {penger}kr")





if __name__ == "__main__":
    main()
