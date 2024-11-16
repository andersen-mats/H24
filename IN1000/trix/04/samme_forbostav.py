personer = {}

while True:
    if input("Vil du fortsette? (j/n)") == "j":
        info = input("Oppi navn og alder: ").split()
        for i in range(len(info)):
            if info[i].isnumeric():
                age = info[i]
                info.pop(i)
                break
        if len(info) > 0:
            name = " ".join(info)
        else:
            name = info[0]
        name.lower()
        personer[name] = age
    else:
        break


while True:
    c = input("Oppgi en bokstav: ").strip().lower()
    if not c.isalpha() and len(c) != 1:
        pass
    else:
        break

for name in personer:
    if name[0] == c:
        print(f"Navn: {name}, alder: {personer[name]}")
    else:
        print("Fant ingen match")

