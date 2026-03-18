# Function para unli-hingi ng numbers at hanapin ang pinakamababa
def find_lowest_number():
    # Start tayo sa 'None' (wala pang laman) kasi wala pa namang tina-type si user
    lowest_number = None

    print("\033[96mEnter numbers (type any letter to stop):\033[0m")

    # Umpisahan na ang infinite loop
    while True:
        try:
            current_number = float(input("\033[96mEnter a number: \033[0m"))
            
            # Kung 'None' pa siya (unang number) OR mas mababa yung bagong type...
            # Papalitan natin yung laman ng lowest_number!
            if lowest_number == None or current_number < lowest_number:
                lowest_number = current_number
                
        except ValueError:
            # Shield on! Pag letter ang tinype, break na agad sa loop.
            print("\033[93mInvalid input detected. Stopping program.\033[0m")
            break