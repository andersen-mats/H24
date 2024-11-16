tall = [i for i in range(1, 11)]

print(tall)

for i in range(len(tall)):
    n = tall[i]
    n = n * n
    tall[i] = n

print(tall)
