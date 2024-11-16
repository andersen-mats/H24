def omvendt_fil(input_file, output_file):
    input_file = open(input_file, "r")
    output_file = open(output_file, "w")
    poem = []
    for line in input_file:
        poem.append(line)
    poem.reverse()
    for line in poem:
        output_file.write(line)
    input_file.close()
    output_file.close()


def main():
    input_file_name = "input.txt"
    output_file_name = "output.txt"
    omvendt_fil(input_file_name, output_file_name)


if __name__ == "__main__":
    main()
