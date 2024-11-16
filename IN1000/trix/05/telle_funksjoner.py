def dobbel(n):
    return n * 2

def check(string, n):
    if len(string) > n:
        return True
    else:
        return False

def length(n):
    n = str(n)
    
    cnt = 0
    for c in n:
        cnt += 1

    return cnt



print(dobbel(30))
print(check("Heihei", 3))
print(length(1415))
