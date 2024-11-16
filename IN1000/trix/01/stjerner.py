print("  * ")
print(" *** ")
print("*****")

# Alternativ versjon:

N = 6 
x = 3

for i in range(N):
    s = N - i - 1
    if i == 0:
        print(' ' * s, end='')
        print('*')
    else:
        print(' ' * s, end='')
        print('*' * x)
        x += 2
