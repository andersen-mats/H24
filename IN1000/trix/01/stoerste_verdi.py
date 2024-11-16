tall1 = int(input('Foerste tall: '))
tall2 = int(input('Andre tall: '))
tall3 = int(input('Tredje tall: '))

big = tall1

if tall2 > big:
    big = tall2

if tall3 > big:
    big = tall3

print(f'Stoerste verdi er: {big}')

mengde = 0 

if tall1 == big:
    mengde += 1
if tall2 == big:
    mengde += 1
if tall3 == big:
    mengde += 1

print(f'{mengde} av tallene har verdi {big}')
