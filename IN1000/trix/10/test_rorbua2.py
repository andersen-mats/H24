from gjest import Gjest
from rorbu import Rorbu

def main():
    rorbua1 = Rorbu()
    rorbua2 = Rorbu()

    rorbua1 = rorbua2

    for i in range(50):
        rorbua1.legg_til_gjest(Gjest())
    for i in range(75):
        rorbua2.legg_til_gjest(Gjest())
    
    print(rorbua1.hent_gjester())
    print(rorbua2.hent_gjester())

    rorbua1.fortell_vits(200)
    rorbua2.fortell_vits(400)

    rorbua1.morsomt()
    rorbua2.morsomt()

if __name__ == "__main__":
    main()
