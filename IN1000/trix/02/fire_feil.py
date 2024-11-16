#tall = input(Tast inn et siffer: ) # to feil: ingen int(), ""

#dobbelt = 2 * tall # tall er ikke int()

#print("Det dobbelte er" dobbel) # Mangler komma, `dobbel` istdnfr `dobbelt`


# Her er forbedret versjon:

tall = int(input("Tast inn et siffer: "))

dobbelt = 2 * tall 

print(f"Det dobbelte er {dobbelt}")
