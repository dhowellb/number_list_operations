# Make a command to print numbers but ignore any duplicates after the first time
def display_first_entries():
    # Gumawa ng box para sa lahat ng numbers na ita-type
    number_list = []
    # Gumawa ng isa pang box para ilista yung mga numbers na nakita na natin
    seen_numbers = []

    # Gumawa ng loop para manghingi ng number 10 times
    for i in range(10):
        current_number = float(input("\033[96mEnter number " + str(i + 1) + ": \033[0m"))
        # Ihulog sa main box yung number
        number_list.append(current_number)

    print("\033[92mNumbers (first entry only for duplicates):\033[0m")

    # Isa-isahin natin check yung mga numbers sa main box
    for current_number in number_list:
        # Kung yung current number ay WALA PA ('not in') sa listahan ng mga nakita na natin...
        if current_number not in seen_numbers:
            # I-print natin siya in yellow text
            print("\033[93m" + str(current_number) + "\033[0m")
            # Tapos ilagay natin siya sa 'seen_numbers' box para pag naulit, i-i-skip na niya!
            seen_numbers.append(current_number)
# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    # Tawagin yung function na ginawa natin sa taas
    display_first_entries()