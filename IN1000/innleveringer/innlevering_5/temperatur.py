def lag_ordbok(filnavn):
    ordbok = {}
    fil = open(filnavn, "r")
    for linje in fil:
        linje = linje.strip("\n").split(",")
        ordbok[linje[0]] = float(linje[1])
    return ordbok


def prosedyre(ordbok, filnavn):
    fil = open(filnavn, "r")
    for linje in fil:
        linje = linje.strip("\n").split(",")
        maaned = linje[0]
        dato = linje[1]
        temp = float(linje[2])
        if temp > ordbok[maaned]:
            print(f"NY VARMEREKORD DEN {dato}. {maaned} PAA {temp} GRADER!")
            ordbok[maaned] = temp
    return ordbok


def skrive(ordbok, filnavn):
    fil = open(filnavn, "w")
    for maaned in ordbok:
        fil.write(f"{maaned},{ordbok[maaned]}\n")


def varmeboelge(filnavn):
    data = {}
    boelge = []
    fil = open(filnavn, "r")
    for linje in fil:
        linje = linje.strip("\n").split(",")
        maaned = linje[0]
        dag = linje[1]
        dato = dag + ". " + maaned
        temp = float(linje[2])
        data[dato] = temp
    cnt = 0
    for dato in data:
        if data[dato] > 25:
            cnt += 1
            boelge.append(dato)
        elif cnt >= 5 and data[dato] <= 25:
            print(f"Varmeboelge fra {boelge[0]} til {boelge[-1]}")
            cnt = 0
            boelge = []
        else:
            cnt = 0
            boelge = []


def main():
    filnavn_max = "max_temperatures_per_month.csv"
    filnavn_2018 = "max_daily_temperature_2018.csv"
    filnavn_skriv = "new_max_temperatures_per_month.csv"
    ordbok = lag_ordbok(filnavn_max)
    ordbok = prosedyre(ordbok, filnavn_2018)
    skrive(ordbok, filnavn_skriv)
    varmeboelge(filnavn_2018)


if __name__ == "__main__":
    main()
