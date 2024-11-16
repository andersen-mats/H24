from gjest import Gjest
from rorbu import Rorbu

def main():

    rorbua = Rorbu()
    for i in range(100):
        rorbua.legg_til_gjest(Gjest())
    
    rorbua.fortell_vits(200)
    rorbua.morsomt()
    rorbua.fortell_vits(1000)
    rorbua.morsomt()

if __name__ == "__main__":
    main()
