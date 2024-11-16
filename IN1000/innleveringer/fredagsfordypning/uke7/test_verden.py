from verden import Verden

verden = Verden()

verden.opprett_dyr("sau", "shaun", 5)
verden.opprett_dyr("sau", "bob", 3)
verden.opprett_dyr("ulv", "slemme", 2)
verden.opprett_dyr("ulv", "ulven", 7)
verden.opprett_dyr("sau", "molly", 1)
verden.opprett_dyr("sau", "cloud", 7)
verden.opprett_dyr("sau", "baaa", 2)
verden.opprett_dyr("sau", "fluffy jr", 6)
verden.opprett_dyr("sau", "snowy", 10)
verden.opprett_dyr("ulv", "blaze", 9)
verden.opprett_dyr("ulv", "fang jr", 4)
verden.opprett_dyr("ulv", "hunter", 8)
verden.opprett_dyr("ulv", "fury", 5)
verden.opprett_dyr("ulv", "raven", 3)

verden.beskriv()

for i in range(10):
    verden.oppdater()

print(f"Den feiteste ulven er: {verden.hent_feit_ulv().hent_navn()}, og han veier: {verden.hent_feit_ulv().hent_vekt()}")

