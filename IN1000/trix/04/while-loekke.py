def splitter(): 
    try:
        inp = input("Skriv fem heltall:\n> ").split()
        inp = [eval(i) for i in inp]
        if len(inp) != 5:
            raise ValueError
    except:
        print("Skriv fem heltall separert med mellomrom")
        return False

    return inp 

def summer(liste):
    sum = 0
    for i in liste:
        sum += i
    print(sum)

def finner(liste):
    for i in liste:
        if i < 10:
            print(i, end=" ")
    print()

def femmer(liste):
    for i in liste:
        if i == 5:
            print("5 er i listen")
            return


def main():
    tall = splitter()
    if tall != False:
        summer(tall)
        finner(tall)
        femmer(tall)
    return 0

if __name__ == "__main__":
    main()

