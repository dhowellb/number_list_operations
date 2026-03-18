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
# I-check muna kung may nakuha ba talagang numbers (kung higit sa zero ang laman ng list)
    # TANDAAN: Siguraduhing pantay ang 'if' na ito sa 'while' na nasa taas para walang error!
    if len(number_list) > 0:
        # Ito yung magic trick! Inaayos nito yung list from lowest to highest.
        number_list.sort()
        
        print("\033[92mNumbers from lowest to highest:\033[0m")
        
        # Isa-isang i-print yung mga nakaayos na numbers
        for current_number in number_list:
            print("\033[93m" + str(current_number) + "\033[0m")
    else:
        # Kung nag-letter agad sa umpisa pa lang:
        print("\033[91mNo valid numbers were entered.\033[0m")

# Ito yung magsisilbing switch para umandar yung buong script
if __name__ == "__main__":
    sort_numbers()