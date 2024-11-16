from math import sqrt

n = int(input("n: "))

primtall = set()
for i in range(2, n):
    p = True
    for x in range(2, int(sqrt(i)) + 1):
        if i % x == 0:
            p = False
            break
    if p:
        primtall.add(i)
    i += 1

print(sorted(primtall))


