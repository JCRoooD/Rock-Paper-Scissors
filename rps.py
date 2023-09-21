from random import randint

t = ["Rock", "Paper", "Scissors"]

def play_game():
    computer = t[randint(0,2)]
    player = False

    while player == False:
        player = input("Rock, Paper, Scissors? Type 'exit' to exit the game.\n")

        if player.lower() == "exit":
            print("Thanks for playing!")
            return
        if player not in t:
            print("That's not a valid play. Check your spelling!")
            player = False
        else:
            if player == computer:
                print("Tie!")
            elif player == "Rock":
                if computer == "Paper":
                    print("You lose!", computer, "covers", player)
                else:
                    print("You win!", player, "smashes", computer)
            elif player == "Paper":
                if computer == "Scissors":
                    print("You lose!", computer, "cut", player)
                else:
                    print("You win!", player, "covers", computer)
            elif player == "Scissors":
                if computer == "Rock":
                    print("You lose...", computer, "smashes", player)
                else:
                    print("You win!", player, "cut", computer)
            else:
                print("That's not a valid play. Check your spelling!")
            computer = t[randint(0,2)]
            player = False
play_game()