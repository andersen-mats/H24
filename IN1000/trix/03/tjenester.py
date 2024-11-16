ord = input("Ord: ")
print(f"Ordet i store bokstaver: {ord.upper()}")
print(f"Lengden til ordet: {len(ord)} tegn")
foerste = ord[0].lower()
print(f"Foerste bokstav: {foerste}")
cnt = 0
for c in ord:
    if c == foerste.lower():
        cnt += 1
print(f"Foerste bokstav forekommer: {cnt} ganger.")
