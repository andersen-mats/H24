from rektangel import Rektangel

rektangel1 = Rektangel(3, 3)
rektangel2 = Rektangel(2, 2)

print("Rektangel1:", rektangel1.info())
print("Rektangel2:", rektangel2.info())

rektangel1.oek_lengde(1)
rektangel2.oek_bredde(2)

print("Rektangel1:", rektangel1.info())
print("Rektangel2:", rektangel2.info())

print("rektangel1 areal:", rektangel1.areal())
print("rektangel2 areal:", rektangel2.areal())

print("rektangel1 omkrets:", rektangel1.omkrets())
print("rektangel2 omkrets:", rektangel2.omkrets())

n = int(input("Reduser: "))
rektangel1.reduser(n)
rektangel2.reduser(n)
