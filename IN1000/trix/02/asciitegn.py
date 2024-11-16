# Du skal ikke å endre disse prosedyrene
def skriv_ascii_1():
    print("   |\---/|\n   | ,_, |")

def skriv_ascii_2():
    print(" -    |``__)/\n--.'(_, |   |\, |")

def skriv_ascii_3():
    print("(__..._(_,..,_..__.'/|\n  '   __\_)/'.....+")

def skriv_ascii_4():
    print("    \_`_/-..----.\n ___/ `   ' ,""+   \\")

def skriv_ascii_5():
    print("(__...'   __\    |`.___.';\n  (_,...'(_,.`__)/'.....+")

def skriv_ascii_6():
    print("(__.._\    .(_,.`__);\n  ../'..'   _  __\_)/+")

def skriv_ascii(): # Mangler ()
    a = True # `true` -> `True`
    b = int("3") # `"3` -> `"3"`
    c = 5 
    if a: #mangler :
        skriv_ascii_1()
    else:
        skriv_ascii_2()
     
    if b + 3 == c: # `=` -> `==`
        skriv_ascii_3()
    elif c > b: 
        skriv_ascii_4() # `("")` -> ()
         
        if a != False: # `fi` -> `if`, `=!`
            skriv_ascii_5() # `asci` -> `ascii`
    else:
         skriv_ascii_6()
 
skriv_ascii()
