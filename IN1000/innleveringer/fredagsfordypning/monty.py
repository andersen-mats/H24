import random

def game(choice, answer):
    # Min logikk. Bak alle dørene er det i utgangspunktet geiter. Kunne sikkert bare brukt en liste, men jeg liker ordbøker.
    doors = {
        0: "goat",
        1: "goat",
        2: "goat",
    }

    # Jeg vil at dette skal føles skikkelig tilfeldig
    doors[random.randint(0, 2)] = "car"
    prize = doors[choice]
    # Jeg vil unngå kræsj, i tilfelle brukeren har valgt en geit
    goats = []

    # Jeg lager en liste med alle geitene som ikke er bak en dør som er valgt av brukeren
    goats = [i for i in range(3) if doors[i] == "goat" and i != choice]
    
    # Verten velger en tilfeldig geitedør og viser frem geiten
    host = random.choice(goats)


    # Kort sagt: Hvis brukeren velger geiten (han vet ikke at han har valgt den), og han bytter dør, så MÅ han få en bil
    # Og omvendt: Har han valgt bilen, og han bytter, MÅ han få en geit.
    if answer == "yes":
        choices = [i for i in range(3) if i != choice and i != host]
        # Her står vi liksom ikke igjen med så særlig mye
        choice = choices[0]
    
    # Dersom brukeren ikke bytter, beholder han sitt innledende valg, og sjansen er altså 1/3 for at det er en bil
    return doors[choice]

def main():
    # Computeren min klarte ikke særlig mye mer enn det
    TESTS = 1000000

    wins = 0

    print(f"There will be {TESTS} test rounds.")

    # Her kunne vi strengt tatt kjørt alt inn i en for-løkke, men hvorfor ikke bare konkretisere den totale tilfeldigheten som definerer programmet
    for _ in range(TESTS):
        choice = random.randint(0, 2)
        prize = game(choice, "yes")
        if prize == "car":
            wins += 1
    win_yes = (wins / TESTS) * 100
    print(f"The player chose to switch doors, and won {win_yes:.4}% of the time.")

    wins = 0
    for _ in range(TESTS):
        choice = random.randint(0, 2)
        prize = game(choice, "no")
        if prize == "car":
            wins += 1
    win_no = (wins / TESTS) * 100
    print(f"The player chose to NOT switch doors, and won {win_no:.4}% of the time.")


if __name__ == "__main__":
    main()