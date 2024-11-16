f = open("navn.txt", "r")

personer = []
hunder = []

for line in f:
    temp = (line.strip("\n").split())
    if temp[0] == "P":
        personer.append(temp[1])
    else:
        hunder.append(temp[1])

f.close()

print("Hunder:")
for name in hunder:
    print(name)
print()
print("Personer:")
for name in personer:
    print(name)
