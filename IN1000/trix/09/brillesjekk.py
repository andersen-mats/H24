def brillesjekk1(styrke):
    ny_styrke = [2.5, 2.75]
    return ny_styrke

def brillesjekk2(styrke):
    styrke[0] = 1.75

def brillesjekk3(styrke):
    styrke = [2.0, 1.75]

# a)

styrke1 = [1.5, 1.5]
brillesjekk1(styrke1)
print(styrke1[0])

# 1.5 skrives ut 

# b)

styrke2 = [1.5, 1.5]
brillesjekk2(styrke2)
print(styrke2[0])

# 1.75 skrives ut

# c)

styrke3 = [1.5, 1.5]
brillesjekk3(styrke3)
print(styrke3[0])

# 1.5 skrives ut
