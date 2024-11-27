def heie(ordbok):
    if ordbok["Brann"] <= 3:
        return "Brann"
    else:
        for k in ordbok:
            if ordbok[k] == 1:
                return k

print(heie({"Rosenborg":2, "Odd":1, "Molde":3, "Brann":4}))
print(heie({"Rosenborg":4, "Odd":1, "Molde":3, "Brann":2}))
