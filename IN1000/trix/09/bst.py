from trenode import Trenode
from random import randint

def main():
    tre = Trenode(randint(1,1000))

    if tre.har_hoyre():
        print("Treet har en verdi nede til hoyre")
    else:
        print("Treet har ikke en verdi nede til hoyre")

    if tre.har_venstre():
        print("Treet har en verdi nede til venstre")
    else:
        print("Treet har ikke en verdi nede til venstre")
    
    for i in range(50):
        tre.utvid(randint(1,1000))

    tre.skrivut()
    print(tre.sortert())
    
    if tre.finn(500):
        print("500 er i treet")
    else:
        print("500 er ikke i treet")

if __name__ == "__main__":
    main()
