from side import Side
from firkant import Firkant

def test_firkant():
    firkant = Firkant()
    assert firkant.er_fullstendig() == False
    sider = Side(10, "gul")
    posisjoner = ["venstre", "hoyre", "oppe", "nede"]

    for posisjon in posisjoner:
        firkant.legg_til_side(sider, posisjon)

    assert firkant.er_fullstendig() == True

    for posisjon in posisjoner:
        firkant.fjern_side(posisjon)

    assert firkant.er_fullstendig() == False
    

    for posisjon in posisjoner:
        firkant.legg_til_side(sider, posisjon)

    firkant2 = Firkant()
    
    liste = [firkant, firkant2]
    print(sjekk_firkanter(liste))
    print(firkant)
    print(firkant2)


def sjekk_firkanter(liste):

    for firkant in liste:
        if not firkant.er_fullstendig():
            return False
    return True

test_firkant()

