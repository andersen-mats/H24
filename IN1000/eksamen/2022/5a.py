def stigespill(terningkast, stiger):

    pos = 0

    for kast in terningkast:
        pos += kast
        if pos in stiger:
            pos = stiger[pos]

    return pos

print(stigespill([5,4,2,2],{5:12, 18:7}))
