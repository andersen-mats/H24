def opp_sukker(sukker):
    mel = 2 * sukker
    smoer = 3 * sukker

    oppskrift = {"sukker": sukker, "mel": mel, "smoer": smoer}

    return oppskrift

def skriv_oppskrift(oppskrift):
    print("Oppskrift paa kaker. Du trenger:")
    for ting in oppskrift:
        print(f"{oppskrift[ting]} gram {ting}")
    

def bak_kaker():
    sukker = int(input("Hvor mye sukker har du? "))
    ordbok = opp_sukker(sukker)
    skriv_oppskrift(ordbok)

bak_kaker()
