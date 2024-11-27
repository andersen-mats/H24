def badmington(per, palle, espen):
    if [per, palle, espen].count(True) == 2:
        return True
    else:
        return False

print(badmington(True, True, False))
print(badmington(True, True, True))
