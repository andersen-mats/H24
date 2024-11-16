match = 0

info = {}

navn1 = input("Navn 1: ").strip().lower()

info[navn1] = list()
info[navn1].append(input("Bosted til navn 1: ").strip().lower())
info[navn1].append(int(input("Alder til navn 1: ")))

navn2 = input("Navn 2: ").strip().lower()
info[navn2] = list()
info[navn2].append(input("Bosted til navn 2: ").strip().lower())
info[navn2].append(int(input("Alder til navn 2: ")))

if len(navn1) == len(navn2):
    match = 60
elif navn1[0] == navn2[0]:
    match = 40
else:
    match = 15

if info[navn1][0] == info[navn2][0]:
    match *= 1.5

age1 = info[navn1][1]
age2 = info[navn2][1]

if age1 < ((age2 / 2) + 7) or age2 < ((age1 / 2) + 7):
    match *= 0.5
elif age1 == age2:
    match *= 1.1

navn = navn1 + navn2
navn_l = [navn1, navn2]

if "t" in navn or "a" in navn:
    match += 2
if "s" and "e" in navn1:
    if "e" not in navn2:
        match += 15
elif "s" and "e" in navn2:
    if "e" not in navn1:
        match += 15

if navn1[0] not in navn2 or navn2[0] not in navn1:
    match -= 20

if navn1[-1] == navn2[0] or navn2[-1] == navn1[0]:
    match += 30

if len(navn1) == 1 or len(navn2) == 1:
    match = 0

match = min(100, match)
match = max(0, match)

print(f"Match er {round(match)}%")
