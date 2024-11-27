def bordsetting(intro, ekstro):
    ret = []
    for i in range(len(intro) * 2):
        if i % 2 == 0:
            ret.append(intro.pop(0))
        else:
            ret.append(ekstro.pop(0))
    return ret

print(bordsetting(["Per","Palle","Espen"], ["Putti", "Plutti", "Pott"]))
