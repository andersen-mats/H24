def sorter_etter_karakter(filnavn):
    info = {}
    f = open(filnavn, "r")
    for line in f:
        temp = line.strip("\n").split(",")
        if temp[1] in info:
            info[temp[1]].append(temp[0])
        else:
            info[temp[1]] = [temp[0]]
    f.close()
    return info


def skriv_ut_sortert(ordbok):
    for key in sorted(ordbok):
        print(f"{key}: {ordbok[key]}")

def hent_vanligste_karakter(ordbok):
    temp = []
    for karakter in ordbok:
        temp.append(len(ordbok[karakter]))
    temp.sort(reverse=True)
    for karakter in ordbok:
        if len(ordbok[karakter]) == temp[0]:
            print(f"{karakter}: {temp[0]}")
        

def main():
    fil = "karakter.csv"
    res = sorter_etter_karakter(fil)
    skriv_ut_sortert(res)
    hent_vanligste_karakter(res)
    

if __name__ == "__main__":
    main()
