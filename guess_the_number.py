import random, time

def guess_the_number():
    print("-----GUESS THE RANDOM NUMBER-----")

    low = int(input("Enter a minimum for the range: "))
    high = int(input("Enter a maximum for the range: "))
    answer = random.randint(low, high)
    guesses = 0
    is_running = True

    print("The computer is selecting a random number...")
    time.sleep(1)

    while is_running:
        guess = int(input(f"Guess a number between {low} and {high}: "))
        guesses += 1
        if guess > answer:
            print("Your guess is too high! Try again.")
            print()
        elif guess < answer:
            print("Your guess is too low! Try again.")
            print()
        elif guess == answer:
            print("You guessed the number!")
            print()
            is_running = False
    print()
    print("------------RESULT---------------")
    print()
    if guesses == 1:
        print("Wow! you guessed the answer with a single guess!")
        print(f"The answer was {answer}")
    else:
        print(f"The answer was {answer}")
        print(f"You guessed {guesses} times")
    
    play_again = input("Would you like to play again(y to play again, anything else to quit) ?: ").lower()
    if play_again == "y":
        guess_the_number()

guess_the_number()


    