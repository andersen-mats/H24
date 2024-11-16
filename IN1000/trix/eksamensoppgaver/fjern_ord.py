setning = "en krabbe skal en dag ut av skallet " 

def forkort_setning(setning, fjern):
    setning = setning.split()
    ny_setning = []
    for ord in setning:
        if ord != fjern:
            ny_setning.append(ord)
    return " ".join(ny_setning)


setning_v2 = forkort_setning(setning, "en")
setning_v3 = forkort_setning(setning_v2, "skal")

print(setning_v2, setning_v3, sep="\n")

