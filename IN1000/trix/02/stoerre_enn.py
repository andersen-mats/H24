tall1 = input("Skriv et tall (f.eks. 11)")
tall2 = input("Skriv et annet tall (f.eks. 7)")
if tall1>tall2:
    print(tall1 + " er storst")
else:
    print(tall2 + " er storst")

# Python interepreteren sjekker str[0] i begge tallene. `999` vil vaere stoerre enn `9`, fordi naar interpreteren ser at begge str[0] er like, saa vil den gaa over til str[1] paa 999, og konkludere med at den er stoerre.
