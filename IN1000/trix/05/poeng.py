def les_poeng(fil):
    poeng = {}
    for line in fil:
        temp = line.strip("\n").split(":")
        poeng[temp[0]] = sum([eval(i) for i in temp[1].split(",")])

    return poeng



f = open("poeng.txt", "r")

res = les_poeng(f)
for navn in res:
    print(navn, res[navn])

f.close()
