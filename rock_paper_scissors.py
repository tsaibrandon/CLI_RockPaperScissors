import random

def main():
    main_menu()

# main menu with game start, exit and game rules
def main_menu():
    select_option = input("Welcome to CL Rock Paper Scissors!"
    "\n----------------------------------"
    "\n           [1] Start              "
    "\n           [1] Exit               "
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
    rps_game()

# player's move
def player_move():
    player_choice = input("Please select one of the following choices:"
    "\n"
    "\nRock"
    "\nPaper"
    "\nScissors"
    "\n"
    "\n"
    )
    return player_choice

# npc move
def npc_move():
    moves = ("Rock", "Paper", "Scissors")
    npc_choice = random.choice(moves)
    return npc_choice

# game mechanics
def rps_game():
    player_points = 0 
    npc_points = 0  
    while player_points < 5 and npc_points < 5:
        player_move()
        npc_move()
        if player_move == "Rock" and npc_move == "Rock":
            print("It's a tie! ")
            pprint(score_board)
        elif player_move == "Rock" and npc_move == "Paper":
            print("You lost! The opponent has gained a point.")
            npc_points + 1
            print(score_board)
        elif player_move == "Rock" and npc_move == "Scissors":
            print("You won! You have gained a point.")
            player_points + 1
            print(score_board)
        elif player_move == "Scissors" and npc_move == "Rock":
            print("You lost! The opponent has gained a point.")
            npc_points + 1
            print(score_board)
        elif player_move == "Scissors" and npc_move == "Paper":
            print("You won! You have gained a point.")
            player_points + 1
            print(score_board)
        elif player_move == "Scissors" and npc_move == "Scissors":
            print("It's a tie! ")
            print(score_board)
        elif player_move == "Paper" and npc_move == "Rock":
            print("You won! You have gained a point.")
            player_points + 1
            print(score_board)
        elif player_move == "Paper" and npc_move == "Paper":
            print("It's a tie! ")
            print(score_board)
        elif player_move == "Paper" and npc_move == "Scissors":
            print("You lost! The opponent has gained a point.")
            npc_points + 1
            print(score_board)
        
# score board
def score_board():
    print(f"You: {player_points}, NPC: {npc_points}")


if __name__ == "__main__":
    main()
