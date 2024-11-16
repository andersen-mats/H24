matrise_en = [                   # matriseTo = [
    [1,4,7],                    #   [1,2,3],
    [2,5,8],       #blir ->     #   [4,5,6],
    [3,6,9]                     #   [7,8,9]
]                               #   ]

def roter(matrise):
    matrise2 = []
    for x in range(len(matrise)):
        rekke = []
        for i in range(len(matrise)):
            rekke.append(matrise[i][x])
        matrise2.append(rekke)
    return matrise2

matrise = roter(matrise_en)

for rekke in matrise:
    print(rekke)
