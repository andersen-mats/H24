from punkt import Punkt

def get_punkt():
    x, y, z = map(int, input("What is x y z? ").split())
    return Punkt(x, y, z)

def les_punkt(filnavn):
    punkter = []
    fil = open(filnavn, "r")
    for linje in fil:
        x,y,z = map(int, linje.strip("\n").split(","))
        punkter.append(Punkt(x, y, z))
    fil.close()
    return punkter

def main():

    fil1 = "gruppe1.csv"
    fil2 = "gruppe2.csv"

    punkter1 = les_punkt(fil1)
    punkter2 = les_punkt(fil2)
    punkt = get_punkt()
    
    gruppe1 = punkt.closest(punkter1)
    gruppe2 = punkt.closest(punkter2)
    if punkt.avstand(gruppe1) < punkt.avstand(gruppe2):
        print("gruppe1")
    else:
        print("gruppe2")

if __name__ == "__main__":
    main()
