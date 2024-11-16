def fib(n):
    sekvens = []
    
    for i in range(n + 1):
        if i == 0:
            sekvens.append(i)
        elif i == 1:
            sekvens.append(i)
        else:
            foo = sekvens[i - 1] + sekvens[i - 2]
            if foo < n:
                sekvens.append(foo)
            else:
                break

    return sekvens

def hent_tall():
    n = int(input("Tall: "))
    l = fib(n)
    for fuck in l:
        print(fuck)

hent_tall()
