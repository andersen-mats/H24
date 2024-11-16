fakta = {
        "norge": {"hovedstad": "oslo", "spraak": "norsk", "kontinent": "europa"},
    "usa": {"hovedstad": "washington", "spraak": "engelsk", "kontinent": "amerika"},
    "yemen": {"hovedstad": "sanaa", "spraak": "arabisk", "kontinent": "asia"},
}

land = input("Hvilket land vil du laere om?\n> ").strip().lower()

if land in fakta:
    info = input("Hva vil du laere?\n> ").strip().lower()
    if info in fakta[land]:
        print(f"{info}: {fakta[land][info]}")
    elif info == "alt":
        print(f"{land} ligger i {fakta[land]['kontinent']} og i {land} snakker de {fakta[land]['spraak']}")
    else:
        print("Har ikke den informasjonen.")
else:
    print("Har ingen info om det landet")    
