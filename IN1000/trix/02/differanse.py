def differanse():
    x = int(input("Oppgi verdien til x:\n"))
    y = int(input("Oppgi verdien til y:\n"))

    diff = x - y

    if diff < 0:
        diff = diff * -1

    print(f"Differansen mellom x og y er {diff}")

differanse()
