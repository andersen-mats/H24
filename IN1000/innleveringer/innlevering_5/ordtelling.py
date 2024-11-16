def lengde(ord):
    antall = 0
    for c in ord:
        antall += 1
    return antall


def ordtelling(setning):
    ordbok = {}
    # "hei" og "hei," er teknisk sett samme ord
    tegn = [",",".",":",";","!","?"]
    for ord in setning.split():
        for c in ord:
            if c in tegn:
                ord = ord.replace(c,"")
        if ord in ordbok:
            ordbok[ord] += 1
        else:
            ordbok[ord] = 1
    return ordbok


def setning_info(setning):
    ordbok = ordtelling(setning)
    # ord: [forekomster, lengde]
    for ord in ordbok:
        ordbok[ord] = [ordbok[ord], lengde(ord)]
    print(f"Det er {len(setning.split())} ord i setningen")
    for ord in ordbok:
        print(f"`{ord}` forekommer {ordbok[ord][0]} ganger og har lengde {ordbok[ord][1]}")


setning = input("Hvilke setning skal vi analysere?\n> ")
setning_info(setning)
