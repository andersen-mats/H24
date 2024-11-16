from buss import Bus

print("Velkommen til bussen.")

buss = Bus(20)

buss.enter(10)

print(buss.info())

buss.enter(12)

print(buss.info())

buss.leave(18)

print(buss.info())

buss.leave(3)
