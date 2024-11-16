from temperatur import Temperature

temp = float(input("Temperatur: "))
instance = input("Hvilken type? ")

obj1 = Temperature(temp, instance)

print(f"""
celcius: {obj1.get_celcius():.4} 
fahrenheit: {obj1.get_fahrenheit():.4} 
kelvin: {obj1.get_kelvin():.4}
""")
