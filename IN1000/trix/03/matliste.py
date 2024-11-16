favorittmat = [
    "lam",
    "salat",
    "suppe",
]

for mat in favorittmat:
    print(mat)

favorittmat.pop(1)

print(len(favorittmat))

for mat in favorittmat:
    print(mat.upper())
