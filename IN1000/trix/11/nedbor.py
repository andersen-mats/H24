from dag import Dag


def les(filnavn):
    dager = []

    fil = open(filnavn, "r")

    for linje in fil:
        linje = linje.strip("\n").split()
        dato = linje[0] + " " + linje[1] + " " + linje[2]
        nedbor = float(linje[4].replace(",", "."))
        dag = Dag(dato, nedbor)
        dager.append(dag)

    fil.close()
    return dager


def dag_maks(dager):
    maks = 0
    for dag in dager:
        if dag.hent_nedbor() > maks:
            maks = dag.hent_nedbor()
            dagen = dag
    return dagen


def tilsammen(dager):
    summen = 0
    for dag in dager:
        summen += dag.hent_nedbor()
    return summen


def beste_maaned(dager):
    maaneder = {
        "januar": 0,
        "februar": 0,        
        "mars": 0,        
        "april": 0,        
        "mai": 0,        
        "juni": 0,        
        "juli": 0,        
        "august": 0,        
        "september": 0,        
        "oktober": 0,        
        "november": 0,        
        "desember": 0,        
    }

    for dag in dager:
        maaned = dag.hent_dato().split()[1]
        if dag.hent_nedbor() == 0:
            maaneder[maaned] += 1
    
    best = 0
    for maaned in maaneder:
        if maaneder[maaned] > best:
            beste_maaned = maaned
            best = maaneder[maaned]
    return beste_maaned


def main():
    filnavn = "nedborsmengder.txt"
    dager = les(filnavn)
    print(f"Paa {dag_maks(dager)}")
    print(f"Til sammen var det {tilsammen(dager):.4} mm nedbor")
    print(f"Den beste maaneden var: {beste_maaned(dager)}")


if __name__ == "__main__":
    main()
