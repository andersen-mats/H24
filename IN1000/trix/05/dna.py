def skriv_dna(fil):
    fil.write(
    """O---o
 O-o
  O
 o-O
o---O\n""")


f = open("dna.txt", "w")

for _ in range(3):
    skriv_dna(f)

f.close()
