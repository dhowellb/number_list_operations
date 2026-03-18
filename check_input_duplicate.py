# Make a command that continuously asks for numbers and checks for duplicates on the fly
def check_input_duplicate():
    # Gumawa ng empty box para ilista yung mga numbers na tinype na
    entered_numbers = []

    # Print instructions so the user knows how to escape the infinite loop
    print("\033[96mEnter numbers (type any letter to stop):\033[0m")

    # Ito yung 'Infinite Loop'. Tuloy-tuloy lang 'to iikot hangga't walang 'break' command.
    while True:
        # Yung 'try' block ay parang shield. Susubukan niyang gawin yung code sa loob...
        try:
            current_number = float(input("\033[96mEnter a number: \033[0m"))
            
            # Check agad kung nasa listahan na yung tinype na number
            if current_number in entered_numbers:
                print("\033[91mDuplicate\033[0m")
            else:
                print("\033[92mUnique\033[0m")
                # Kung bago yung number, ihulog sa box natin para matandaan next time
                entered_numbers.append(current_number)
                
        # Kung nag-type ng letter yung user, mag-e-error dapat yung 'float()'. 
        # Sasaluhin ng 'except ValueError' yung error na 'yon para hindi mag-crash yung buong program!
        except ValueError:
            print("\033[93mInvalid input detected. Stopping program.\033[0m")
            # Yung 'break' ang papatay sa 'while True' loop para makapag-stop na nang maayos
            break
# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    # Tawagin yung function para mag-start na yung infinite loop
    check_input_duplicate()