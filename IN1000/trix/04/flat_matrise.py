eksempel_matrise = [[0, 1, 2], 
                    [3, 2, 1], 
                    [1, 1, 0]]

ny = list()
for rekke in eksempel_matrise:
    for n in rekke:
        ny.append(n)

print(ny)

eksempel_3d_matrise = [
    [[0, 1, 2], [3, 2, 1]], 
    [[1, 1, 0], [4, 2, 3], [2, 1, 0]]
    ]

ny3d = list()

for element1 in eksempel_3d_matrise:
    for element2 in element1:
        for element3 in element2:
            ny3d.append(element3)

print(ny3d)
