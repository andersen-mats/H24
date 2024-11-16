string = str(input('String: '))
integer = int(input('Integer: '))
floating = float(input('Float: '))

print(type(string))
print(type(integer))
print(type(floating))

#type(integer) kan ikke gjoere om strengen 3.8 til et heltall

print(type(integer * string))
print(type(integer * floating))
#print(type(string * floating))

# Du kan ikke gange en string med en float; det gir ingen mening

print(int(floating))

# Naar et flyttall konverteres til et rundt tall, saa rundes det ned
