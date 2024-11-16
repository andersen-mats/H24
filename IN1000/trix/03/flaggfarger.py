def color(colors):
    if len(colors) == 3:
        for n in colors:
            if n not in range(256):
                return False
    else:
        return False

    return True




def main():
    inp = input("Skriv tre tall med mellomrom:\n> ").split()
    inp = [eval(i) for i in inp]
    print(type(inp))
    if color(inp):
        print("Alt gikk fint. Numrene korresponderer til en farge.")
    else:
        print(f"De tre tallene maa vaere mellom 0 og 256")
main()
