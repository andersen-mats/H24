# Sukker
def main():
    
    # Spoer om brukeren vil ha en brus
    svar = input("Har du lyst paa en brus? (ja/nei)\n> ").lower()
    
    # Beslutningsmoenster hvis utfall avhenger av hva brukeren svarte
    if svar == "ja":
        print("Her har du en brus!")
        print("""
            _                                   
          .!.!.                             
           ! !                                   
           ; :                                
          ;   :                                
         ;_____:                                 
         ! COKE!                                 
         !_____!                                 
         :     :
         :     ;                                       
         .'   '.                             
         :     :                             
          '''''
""")

    elif svar == "nei":
        print("Den er grei.")
    else:
        print("Det forstod jeg ikke helt ...")
    
    # Sukker
    return 0

# Dette sukkeret er strengt tatt ikke noedvendig, men
# jeg liker aa gjoere det, fordi jeg anser det
# som en slags `god vane` ...
if __name__ == "__main__":
    main()
