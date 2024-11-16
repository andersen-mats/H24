# a)
gammelString = "abc"
nyString = gammelString
nyString += "d"
print(gammelString)

# `abc` printes ut, fordi strings er immutable

# b)
gammelListe = ["a", "b", "c"]
nyListe = gammelListe
nyListe += ["d"]
print(gammelListe)

# `["a","b","c","d"]` skrives ut, fordi lister er mutable

# c)
gammelOrdbok = {"a":1, "b":2, "c":3}
nyOrdbok = gammelOrdbok
nyOrdbok["d"] = 4
print(gammelOrdbok)

# `a1 b2 c3 d4` skrives ut

# d)
gammelMengde = {"a", "b", "c"}
nyMengde = gammelMengde
nyMengde.add("d")
print(gammelMengde)

# `a b c d` skrives ut
