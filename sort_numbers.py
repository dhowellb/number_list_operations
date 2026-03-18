# Function para humingi ng maraming numbers at ayusin mula lowest to highest
def sort_numbers():
    # Gumawa ng empty box para hakutin lahat ng ita-type
    number_list = []

    print("\033[96mEnter numbers (type any letter to stop):\033[0m")

    # Umpisahan ang infinite loop para sa unli-inputs
    while True:
        try:
            current_number = float(input("\033[96mEnter a number: \033[0m"))
            # Ihulog agad sa box natin yung valid number
            number_list.append(current_number)
            
        except ValueError:
            # Shield on! Pag nag-type ng letter, wag i-crash. I-break lang ang loop.
            print("\033[93mInvalid input detected. Sorting now...\033[0m")
            break