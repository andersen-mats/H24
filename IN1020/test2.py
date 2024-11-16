matrise = [[x for x in range(10000)] for y in range(10000)]
sum = 0
for i in range(len(matrise)):
    for j in range(len(matrise[i])):
        sum += matrise[j][i] 
