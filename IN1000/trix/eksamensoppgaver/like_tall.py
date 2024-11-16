def like(liste):

    ref = liste[0]

    for n in liste:
        if n != ref:
            return -1

    return ref


print(like([-1,-1,-1]))

# Vi kan ikke vaere sikre paa at ikke alle tallene i listen var like dersom vi faar -1,
# for listen kan inneholde kun -1
