def process(text, file_name, n):
    file = open(file_name, "w")
    text = text.split()
    count = 0
    for word in text:
        if len(word) + count > n:
            word += " " 
            count = len(word)
            word = "\n" + word
        else:
            word += " "
            count += len(word)
        file.write(word)
    file.close()


def main():
    file_name = "maks_tegn.txt"
    text = input("Skriv din tekst:\n> ")
    n = int(input("Maksimalt antall tegn pr. linje:\n> "))
    process(text, file_name, n)

if __name__ == "__main__":
    main()
