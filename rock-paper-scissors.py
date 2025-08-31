import random

def RPS():

    options = ("rock", "paper", "scissors")
    win_conditions = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    player_score = 0
    computer_score = 0

    while True:
        computer = random.choice(options)
        player = input("Enter rock, paper or scissors (rock, paper or scissors): ")
        print()

        if player == computer:
            print(f"You both entered {computer}, it's a draw!")
            print()
            print(f"Player: {player_score}   |   Computer: {computer_score}")
            print()
        elif win_conditions[player] == computer:
            print(f"You chose {player}, computer chose {computer}, you won this round!")
            player_score += 1
            print()
            print(f"Player: {player_score}   |   Computer: {computer_score}")
            print()
        else:
            print(f"You chose {player}, computer chose {computer}, computer won this round!")
            computer_score += 1
            print()
            print(f"Player: {player_score}   |   Computer: {computer_score}")
            print()
        if player_score == 5 or computer_score == 5:
            print()
            print("-----------------RESULT-----------------")
            print()
            if player_score == 5:
                print("The winner is Player")
            elif computer_score == 5:
                print("The winner is Computer")
            print(f"Player: {player_score}   |   Computer: {computer_score}")
            break

RPS()
play_again = input("Do you want to play again(y to play again, anything else to quit)?: ")
if play_again == "y":
    RPS()




