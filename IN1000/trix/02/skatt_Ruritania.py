def skatt(inntekt):
    TERSKEL = 10000
    if inntekt >= TERSKEL:
        rest = inntekt - TERSKEL
        skatt = TERSKEL * 0.1 + rest * 0.3
        return skatt
    else:
        skatt = inntekt * 0.1
        return skatt
    
def main():
    inntekt = float(input("Tast inn din inntekt:\n> "))
    print(f"Skatt: {skatt(inntekt)}")


main()
