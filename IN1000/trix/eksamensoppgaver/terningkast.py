def terningkast():

    tell = 0
    for x in range(1,7):
        for y in range(1,7):
            for z in range(1,7):
                print(x,y,z)
                temp = [x,y,z]
                if len(set(temp)) <= 2:
                    tell += 1
                    
    print(f"{tell} kast hadde 2 eller like terninger")


terningkast()

