import random, time

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐️"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("************")
    print()
    print(" | ".join(row))
    print()
    print("************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        match row[0]:   
            case '🍒':  
                return bet * 10
            case '🍉':
                return bet * 25
            case '🍋':
                return bet * 50
            case '🔔':
                return bet * 100
            case '⭐️':
                return bet * 777
            case _:
                print("Oops, something went wrong...")
                return 0
    else:
        return 0


def main():
    balance = 1000
    print("************************")
    print("Welcome to Python slots!")
    print("************************")
    print("Here are the following payouts for each symbol you get 3 in a row of:")
    print("🍒: 10x")
    print("🍉: 25x")
    print("🍋: 50x")
    print("🔔: 100x")
    print("⭐️: 777x")

    while balance > 0:
        print(f"Your balance is ${balance}")

        bet = input("Place your bet (or q to quit): ")

        if bet.lower() == "q":
            break

        if not bet.isdigit():
            print("Enter a valid number please")
            continue
        
        bet = int(bet)

        if bet > balance:
            print("You don't have enough money to bet this much")
            continue
            
        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet
        print("Spinning...\n")
        row = spin_row()
        time.sleep(0.5)
        print_row(row)
        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!")
            balance += payout
        else:
            print("You lost")

    if balance == 0:
        print("You have no money left")
  
    play_again = input("Do you want to play again (type y to play again, type anything else to quit)?: ")
    if play_again.lower() == "y": 
        main() 
     
    
if __name__ == '__main__':
    main()
print("Thanks for playing!") 