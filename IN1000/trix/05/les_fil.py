f = open("navn.txt", "r")

navn_liste = list()

for navn in f:
    navn_liste.append(navn)

navn_liste = [line.rstrip("\n") for line in navn_liste]

f.close()

print(navn_liste)
