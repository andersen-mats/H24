def fil_na_filter(input_filnavn, output_filnavn):
   
    input_fil = open(input_filnavn, "r")
    output_fil = open(output_filnavn, "w")

    for line in input_fil:
        if "NA" not in line:
            output_fil.write(line)

    input_fil.close()
    output_fil.close()

def main():
    fil_na_filter("input_med_na.csv", "output_uten_na.csv")


main()
