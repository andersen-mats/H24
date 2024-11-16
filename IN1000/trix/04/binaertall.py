def main():
    tall = int(input("Skriv et tall: "))
    binaer = []
    while tall != 0:
        res = tall % 2
        tall = tall // 2
        binaer.insert(0, str(res))

    resultat = "".join(binaer)
    print(resultat)
    
    return 0

if __name__ == "__main__":
    main()

