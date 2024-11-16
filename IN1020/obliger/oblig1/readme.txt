FORKLARING:

Programmet kjoerer i en loekke, helt til brukeren
taster inn korrekt PLU-kode, eller taster 0.

Det sjekker hvilken PLU-kode det er vha. BRZ-kommandoen.

Eple har plu-koden 111, tomat har plu-koden 222.

Naar en korrekt PLU-kode er registrert, maa brukeren taste inn antall.
Viktig: dersom brukeren her taster inn 0, vil programmet spoerre igjen.

Deretter outputes en rekke informasjon om varen: stempler og holdbarhet.

vha. OTC og ascii-verdien: 

N = Nyt Norge-stempelet
E = Eco-stempelet
S = 5-om-dagen-stempelet (sunnhet)

Jeg har valgt aa kjoere OTC paa verdien 10, som i ascii representerer \n,
mellom hver utskrift. Ellers ble det bare rotete.

Holdbarhet outputes som et enkelt heltall. Eplet er holdbart i 6 dager,
tomaten er holdbar i 4 dager.

Antallet ganges med varens pris, og legges til i summen.

Dette gjoeres ved aa subtrahere 1 fra antall varer for hver runde i loekken;
BRZ kommer fra BRA, og soerger for at den gaar paa rundgang, frem til alle
varene er registrert. 

Deretter returnerer programmet tilbake til start.
Dersom brukeren naa taster inn 0, vil programmet skrive ut summen,
for deretter aa skrive ut mitt UiO-brukernavn, "MATANDE". Dette gjoeres
for oevrig med selvmodifiserende kode.

UTFORDRINER:

Min desidert stoerste utfordring, var plass.

Det var et mareritt for meg aa optimalisere programmet, gitt plassmangelen.

Egentlig hadde jeg grandiose planer for programmet; jeg ville ha 3 for 2 tilbud
og begrenset antall varer tilgjengelige, men jeg fikk bare ikke plass til det.

Jeg ville ogsaa outputte at varene kom fra USA og UK (korte navn), men igjen:
Det var bare for lite plass tilgjengelig.

Jeg kunne faatt til mer, dersom jeg ikke hadde maattet skrive ut
mitt UiO-brukernavn paa slutten, siden selvmodifiserende kode tar en del plass,
men la gaa.

Det var en veldig goey og givende oppgave.

