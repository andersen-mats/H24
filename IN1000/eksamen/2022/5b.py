def stigespill(terningkast, stiger):

    pos = 0

    for kast in terningkast:
        pos += kast
        if pos in stiger:
            pos = stiger[pos]

    return pos

def hvilke_tre_kast(slutt_rute, stiger):
    ret = []

    for x in range(1,7):
        for y in range(1,7):
            for z in range(1,7):
                temp = [x,y,z]
                if stigespill(temp,stiger) == slutt_rute and temp not in ret:
                    ret.append(temp)
    return ret
                                
    

print(stigespill([5,4,2,2],{5:12, 18:7}))
print(hvilke_tre_kast(5, {3:15, 17:4}))
