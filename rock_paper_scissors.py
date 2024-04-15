import random

player_points = 0
npc_points = 0 

def main():
    main_menu()

# main menu with game start, exit and game rules
def main_menu():
    select_option = input("Welcome to CL Rock Paper Scissors!"
    "\n----------------------------------"
    "\n           [1] Start              "
    "\n           [2] Exit               "
    "\n"
    )

    if select_option == "1":
        start_game()
    elif select_option == "2":
        print("Bye bye!")
        exit()
    else:
        print("Invalid choice!")
        main_menu()

# the game itself
def start_game():
    print(
        "\nThe rules are simple: "
        "\n"
        "\n     Rock beats scissors"
        "\n     Paper beats rock"
        "\n     Scissors beat paper"
        "\n"
        "\nThe first to 5 points wins!"
        "\n"
    )
    while player_points <= 5 and npc_points <= 5:
        if player_points == 5 and npc_points != 5:
            win()
        elif player_points != 5 and npc_points == 5:
            lose()
        else:
            game_rules(player_move(), npc_move())
    exit()

# player's move
def player_move():
    player_choice = input("Please select one of the following choices:"
    "\n"
    "\n[1] Rock"
    "\n[2] Paper"
    "\n[3] Scissors"
    "\n"
    "\n"
    )
    # print(player_choice)
    return player_choice
    

# npc move
def npc_move():
    moves = ("Rock", "Paper", "Scissors")
    npc_choice = random.choice(moves)
    print(f"NPC chose: {npc_choice}")
    return npc_choice
    

# game mechanics
def game_rules(player_move, npc_move,):
    global player_points
    global npc_points
    if player_move == "1" and npc_move == "Rock":
        print("It's a tie! ")
        score_board()
    elif player_move == "1" and npc_move == "Paper":
        print("You lost! The opponent has gained a point.")
        npc_points += 1
        score_board()
    elif player_move == "1" and npc_move == "Scissors":
        print("You won! You have gained a point.")
        player_points += 1
        score_board()
    elif player_move == "3" and npc_move == "Rock":
        print("You lost! The opponent has gained a point.")
        npc_points += 1
        score_board()
    elif player_move == "3" and npc_move == "Paper":
        print("You won! You have gained a point.")
        player_points += 1
        score_board() 
    elif player_move == "3" and npc_move == "Scissors":
        print("It's a tie! ")
        score_board()
    elif player_move == "2" and npc_move == "Rock":
        print("You won! You have gained a point.")
        player_points += 1
        score_board()
    elif player_move == "2" and npc_move == "Paper":
        print("It's a tie! ")
        score_board()
    elif player_move == "2" and npc_move == "Scissors":
        print("You lost! The opponent has gained a point.")
        npc_points += 1
        score_board()

# what happens when you reach 5 points
def win():
    restart = input("Congradulations! You won!"
    "\nWould you like to play again?"
    "\n[1] Yes"
    "\n[2] No"
    )
    if restart == "1":
        start_game()
    elif restart == "2":
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid option!")
        win()

# what happens when you lose
def lose():
    restart = input("Better luck next time!"
    "\nWould you like to play again?"
    "\n"
    "\n[1] Yes"
    "\n[2] No"
    "\n"
    )
    if restart == "1":
        start_game()
    elif restart == "2":
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid option!")
        lose()
     
# score board
def score_board():
    print(f"You: {player_points}, NPC: {npc_points}")

if __name__ == "__main__":
    main()
