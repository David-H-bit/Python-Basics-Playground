import random

def calculate_total(hand):
    current_total = 0
    aces = 0
    for card in hand:
        if card in ["J", "Q", "K"]:
            current_total += 10
        elif card == "A":
            current_total += 11
            aces += 1
        else:
            current_total += int(card)
        while current_total > 21 and aces > 0:
            current_total -= 10
            aces -= 1
    return current_total


def game_of_blackjack():

    money = 1000
    while money > 0:
        cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        deck = cards * 4 # 52 card deck

        random.shuffle(deck)

        player_deck = [deck.pop(), deck.pop()]
        dealer_deck = [deck.pop(), deck.pop()]

        print(f"You currently have ${money}")

        while True:
            bet = int(input("How much will you wager?: "))
            if bet > money or bet < 0:
                print("You cannot enter more than what you have, 0 or lower than 0")
            else:
                break

        money -= bet
        print(f"You currently have ${money}")

        player_total = calculate_total(player_deck)
        dealer_total = calculate_total(dealer_deck)

        if player_total == 21 and dealer_total == 21:
            print("You both got blackjack, it's a draw! you get your money back")
        elif player_total == 21:
            print("You got a blackjack!")
            money += (bet * 2)
            print(f"Your cards are: {player_deck[0]} and {player_deck[1]}")
            break

        elif dealer_total == 21:
            print("The dealer a blackjack!")
            print(f"The dealer's cards are: {dealer_deck[0]} and {dealer_deck[1]}")
            break


        print(f"Your cards are: {player_deck[0]} and {player_deck[1]}")
        print(f"The dealer has a {dealer_deck[0]}")


        while True:
            decision = input("Would you like to hit (type h) or stand(type s)?: ").lower()
            if decision == "h":
                new_card = deck.pop()
                player_deck.append(new_card)
                print(f"You drew: {new_card}")
                print(f"Your cards: {player_deck}")

                player_total = calculate_total(player_deck)
                if player_total > 21:
                    print("Your total is higher than 21, you lose!")
                    break

            elif decision == "s":
                player_total = calculate_total(player_deck)
                print(f"Your total is {player_total}")
                print(f"The dealer has {dealer_deck[0]} and {dealer_deck[1]}")

                while calculate_total(dealer_deck) < 17:
                    print("The dealer is pulling a card...")
                    dealer_deck.append(deck.pop())
                    dealer_total= calculate_total(dealer_deck)
                    print(f"Dealer's deck: {dealer_deck}")
                    print(f"The dealer has {dealer_total}")
                    if dealer_total > 21:
                        print("The dealer's total is higher than 21, you win!")
                        money += (bet * 2)
                        break

                if player_total < dealer_total <= 21:
                    print("The dealer wins!")
                elif player_total == dealer_total:
                    print("It's a draw, you get your money back")
                    money += bet
                else:
                    print("You win!")
                    money += (bet * 2)
                break

    play_again = input("You ran out of money! Do you want to play again (y to play again, anything else to exit)?: ")
    if play_again.lower() == "y":
        game_of_blackjack()
    else:
        print("Thanks for playing!")

game_of_blackjack()
