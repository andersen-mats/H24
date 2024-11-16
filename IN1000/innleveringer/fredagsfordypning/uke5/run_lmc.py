from les_lmc import les_program

def hlt():
    """
    Avslutter programmet, opkode 0
    """
    exit(0)

def IO():
    """
    IO-opperasjoner, opkode 9. 
    Definerte opperasjoner er 
    addr = 1 : input
    addr = 2 : output
    addr = 22: ASCII-output
    """
    pass


def kjor_program(minne):
    ## Programmet skal kjøre helt til vi når en hlt-instruksjon, som er 0xx.
    opperasjoner = {
            0 : hlt,
            9 : IO
        } 
    # Dette er alle registrene til LMC
    akkumulator           = 0 # Hovedregister
    programteller         = 0 # peker på neste instruksjon i minnet
    instruksjons_register = 0 # Holder på opperasjonskoden
    minneadresse_register = 0 # Viser til minneadressen assosiert med en instruksjon.

    for i in range 

program = "add.txt"
minne = les_program(program)
kjor_program(minne)
