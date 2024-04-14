import random

def main():
    main_menu()

# main menu with game start, exit and game rules
def main_menu():
    choice = input("Welcome to CL Rock Paper Scissors!"
    "\n----------------------------------"
    "\n           [1] Start              "
    "\n           [1] Exit               "
    )

    if choice == "1":
        start_game()
    elif choice == "2":
        print("Bye bye!")
        exit()
    else:
        print("Invalid choice!")
        main_menu()
    
    # "\nThe rules are simple: "
    # "\n     Rock beats scissors"
    # "\n     Paper beats rock"
    # "\n     Scissors beat paper"
    # "\n                    "
    # "\nThe first to 5 points wins!"

# the game itself
def start_game():
    print("Time to play!")

if __name__ == "__main__":
    main()
