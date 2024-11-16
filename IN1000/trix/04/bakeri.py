bakeri = {}

def menyen(meny):
    meny["Croissant"] += 10
    for vare in meny:
        print(f"Vare: {vare}, pris: {meny[vare]}")
    print()


bakeri["Croissant"] = 25
bakeri["Grovbroed"] = 40
bakeri["Kneippbroed"] = 20
bakeri["Rosinbolle"] = 20
bakeri["Baguette"] = 10

menyen(bakeri)
menyen(bakeri)
