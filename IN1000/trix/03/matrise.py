liste_noestet = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9],
]

print(liste_noestet[0][0])
print(liste_noestet[1][2])
print(liste_noestet[2][1])

sum_kolonne = 0
sum_rad = 0

for i in range(len(liste_noestet)):
    sum_kolonne += liste_noestet[i][0]

for i in liste_noestet[0]:
    sum_rad += i

print(sum(liste_noestet[0]))

print(sum_kolonne, sum_rad)
