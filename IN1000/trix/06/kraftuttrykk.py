def skriv_med_trykk(streng):
    print(streng + "!")

for i in range(5):
    streng = input("streng: ")
    if streng == "nei":
        break
    else:
        skriv_med_trykk(streng)
