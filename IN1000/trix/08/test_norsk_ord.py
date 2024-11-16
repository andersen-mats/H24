from norsk_ord import NorskOrd

ord1 = NorskOrd("høst")
ord2 = NorskOrd("vinter")
ord3 = NorskOrd("vår")
ord4 = NorskOrd("sommer")

tegn = {"æ": "ae", "ø": "oe", "å": "aa"}
liste = [ord1,ord2,ord3,ord4]

for element in liste:
    foo = element.hent_ord()
    for c in foo:
        if c in tegn:
            bar = foo.replace(c, tegn[c])
            element.endre_ord(bar)
    print(element.hent_ord())
