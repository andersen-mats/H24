def main():
    navn = input('Hva er ditt navn? ').strip().title()
    
    for _ in range(3):
        si_hei()
    
    print(navn)

def si_hei():
    print('hei')

if __name__ == '__main__':
    main()
