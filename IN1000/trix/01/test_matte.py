quiz = {
    '1 + 1 = ': '2',
    '34 + 3 = ': '37',
    '3 * 3 = ': '9',
}

has_lost = False

for question in quiz:
    answer = input(question).strip().lower()
    if answer == quiz[question]:
        print('Riktig!') 
    else:
        print('Det var feil. Spillet er over.')
        has_lost = True
        break

if not has_lost:
    print('Gratulerer, du vant!')
