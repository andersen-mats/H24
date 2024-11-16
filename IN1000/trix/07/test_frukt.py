from frukt import Fruit

eple = Fruit("eple", 100, True)
paere = Fruit("paere", 25, True)
jordbaer = Fruit("jordbaer", 5, True)
banan = Fruit("banan", 87, True)
trollhegg = Fruit("trollhegg", None, False)
slyng = Fruit("slyng", None, False)
kiwi = Fruit("kiwi", 84, True)
dadler = Fruit("dadler", 41, True)
aprikos = Fruit("aprikos", 20, True)
melon = Fruit("melon", 99, True)
granateple = Fruit("granateple", 111, True)

frukter = [
    eple,
    paere,
    jordbaer,
    banan,
    trollhegg,
    slyng,
    kiwi,
    dadler,
    aprikos,
    melon,
    granateple
]

spiselige_vann_frukter = []

for frukt in frukter:
    if isinstance(frukt.water, (int, float)) and frukt.water > 85 and frukt.eat == True:
        spiselige_vann_frukter.append(frukt)

for frukt in spiselige_vann_frukter:
    print(frukt.get_name())
