def fak(n):
    if n == 0:
        return 1

    n = n * fak(n - 1)

    return n


def dobbel(n):
    if n == 0:
        return 0

    n = dobbel(n - 1) + 2

    return n


def fib(n):
    if n == 0 or n == 1:
        return 1

    n = fib(n - 1) + fib(n - 2)

    return n


n = int(input())

print(fak(n))
print(dobbel(n))
print(fib(n))
