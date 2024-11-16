def samlet_vaksinasjon(krav_hvert_land):

    alle_vaksiner = list()

    for land in krav_hvert_land:
        for vaksine in land:
            alle_vaksiner.append(vaksine)

    alle_vaksiner = set(alle_vaksiner)
    
    return list(alle_vaksiner)

def test_samlet_vaksinasjon():

    alle_vaksiner = [["difteri", "hepatit", "gulfeber"], ["gulfeber", "hepatit", "corona"], ["meslinger", "corona", "tsetse"], ["gulfeber", "meslinger"], ["corona", "difteri"]]

    print(samlet_vaksinasjon(alle_vaksiner))

test_samlet_vaksinasjon()
