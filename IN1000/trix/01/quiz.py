spor1 = 'Hva er Norges hovedstad? '
spor2 = 'Er Spania et monarki? '
spor3 = 'Er Pluto en planet? '

svar1 = 'oslo'
svar2 = 'ja'
svar3 = 'nei'

quiz = {
    spor1: svar1,
    spor2: svar2,
    spor3: svar3,
}

for spors in quiz:
    if input(spors).strip().lower() == quiz[spors]:
        print('korrekt!')
    else:
        print(f'feil, svaret var: {quiz[spors]}')
