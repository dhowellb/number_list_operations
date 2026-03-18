# Make a command to find numbers that don't have any twins/duplicates
def display_unique_numbers():
    # Gumawa ng empty list na parang kahon para saluhin yung numbers
    number_list = []

    # Gumawa ng loop para manghingi ng number 10 times
    for i in range(10):
        current_number = float(input("\033[96mEnter number " + str(i + 1) + ": \033[0m"))
        # Ihulog yung number na tinype ni user sa loob ng list natin
        number_list.append(current_number)

    print("\033[92mNumbers without duplicates:\033[0m")

    # Isa-isahin natin check yung laman ng list
    for current_number in number_list:
        # Kapag eksaktong isa lang ang bilang niya sa loob ng list (walang duplicate)
        if number_list.count(current_number) == 1:
            print("\033[93m" + str(current_number) + "\033[0m")
# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    # Tawagin yung function na ginawa natin sa taas
    display_unique_numbers()