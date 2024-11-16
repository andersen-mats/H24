def main():

    stopp = 3
    plasser = 30
    
    for stopp in range(1, stopp + 1):
        venter = int(input(f"Stasjon {stopp}! Hvor mange venter paa bussen?\n> "))

        if plasser - venter >= 0:
            plasser -= venter
            print(f"{venter} gaar ombord")
        else:
            gaa = (plasser - venter) * -1
            plasser -= venter - gaa
            print(f"Bussen er full. {gaa} maa gaa til fots.")


    print(f"Bussen er fremme med {30 - plasser} ombord")

if __name__ == "__main__":
    main()
