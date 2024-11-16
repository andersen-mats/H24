def kalkulator(tall1, operasjon, tall2):

    if operasjon == "+":
        return tall1 + tall2
    elif operasjon == "-":
        return tall1 - tall2
    elif operasjon == "*":
        return tall1 * tall2
    elif operasjon == "/":
        return tall1 / tall2
    else:
        return tall1 % tall2


def main():

    operasjoner = ["+", "-", "*", "/", "%"]

    try:
        input1 = float(input("Foerste tall: ").strip())
        input2 = input("Operasjon: ").strip()
        if input2 not in operasjoner:
            raise TypeError
        input3 = float(input("Andre tall: ").strip())
    except ValueError:
        print("Ulovlige argumenter")
        return 1
    except TypeError:
        print("Ulovlig operasjon")
        return 2
    
    resultat = kalkulator(input1, input2, input3)

    if input1 % 1 == 0:
        input1 = int(input1)
    if input3 % 1 == 0:
        input3 = int(input3)
    if resultat % 1 == 0:
        resultat = int(resultat)
        print(f"{input1} {input2} {input3} = {resultat}")
    else:
        print(f"{input1} {input2} {input3} = {resultat:.5}")

    return 0


main()
