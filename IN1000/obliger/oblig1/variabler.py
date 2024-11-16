# Sukker
def main():

    # Skriver ut `Hei student!` i terminalen
    print("Hei student!")

    # Spoer brukeren om navnet, lagrer i variabelen `navn`
    navn = input("Hva er navnet ditt?\n> ")

    # Printer ut strengen som er lagret i variabelen `navn` vha. f-streng
    print(f"Hei {navn}!")

    # Definerer to heltallsverdier x og y
    x = 5
    y = 7
    
    # Printer ut heltallsverdiene i terminalen paa hver sin linje
    print(f"x: {x}\ny: {y}")
    
    # Regner ut differansen mellom x og y, lagrer den i `dif`
    dif = x - y

    # Printer ut differansen
    print(f"Differanse: {dif}")

    # Ber brukeren om enda et navn ...
    nytt_navn = input("Gi meg enda et navn:\n> ")
    
    # Slaar sammen det foerste og det andre navnet
    sammen = navn + nytt_navn

    # Printer `sammen`
    print(sammen)

    # Endrer `sammen` til aa inkludere `og`
    sammen = navn + " og " + nytt_navn

    # Printer den nye verdien til `sammen`
    print(sammen)

    # Sukker
    return 0

# Sukker
if __name__ == "__main__":
    main()
