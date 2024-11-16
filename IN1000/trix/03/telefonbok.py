telefonbok = {
    "Arne": 22334455, 
    "Lisa": 95959595,
    "Jonas": 97959795, 
    "Peder": 12345678,
}

navn = input("Skriv et navn:\n> ").strip().title()
if navn in telefonbok:
    print(f"{navn} sitt tlf.nr. er {telefonbok[navn]}")
else:
    nummer = int(input("Kjenner ikke nr. Hva er nr.?\n> ").strip())
    telefonbok[navn] = nummer
