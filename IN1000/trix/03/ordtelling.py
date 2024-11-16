ordliste = ["I", "dag", "er", "jeg", "så", "lykkelig", "så", "lykkelig", "så", "lykkelig", "det", "hele", "endte", "dejligt", "jeg", "synger", "og", "er", "glad", "Ja", "alting", "endte", "lykkeligt", "så", "lykkeligt", "så", "lykkeligt", "i", "dag", "er", "jeg", "så", "lykkelig", "som", "dagen", "den", "er", "lang"]

print(f"Det er {len(ordliste)} ord i listen")

unike = set(ordliste)

print(f"Det er {len(unike)} unike ord i ordlisten")

ordbok = {}

samle = ["lykkelig", "dag", "så"]

for ord in ordliste:
    if ord in samle:
        if ord in ordbok:
            ordbok[ord] += 1
        else:
            ordbok[ord] = 1

for ord in ordbok:
    print(f"`{ord}` forekommer {ordbok[ord]} ganger")

print(f"Dette er orboken: {ordbok}")
print(f"Dette er ordboken med list(): {list(ordbok)}")
print(f"Dette er ordboken med set(): {set(ordbok)}")
print("list() paa ordbok gjoer den om til en liste, uten verdiene")
print("set() tar vekk alle verdiene, og gjoer den til et sett, uten duplikater.\nMerk at dict ikke tillater duplikater uansett.")
