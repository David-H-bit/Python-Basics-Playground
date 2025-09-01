import random

words = (
    "awkward", "rhythm", "glimpse", "subtle", "genuine",
    "whisper", "honest", "island", "chaos", "drought",
    "echoes", "lengths", "scheme", "winter", "knock",
    "muscle", "honor", "doubt", "stretch", "plague"
)

def display(x):
    print(" ".join(x))
    print()

def play_game():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    guesses = 6
    guessed_letters = set()

    while True:
        print(f"Guesses left: {guesses}")
        display(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha() or guess == " ":
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} has already been guessed")
            continue
        
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i] = guess
        else:
            guesses -= 1

        if "_" not in hint:
            print(f"Congrats, you won! the answer was {answer}")
            break

        if guesses == 0:
            print(f"You are out of guesses! The answer was {answer}")
            break

def main():
    while True:
        play_game()
        play_again = input("Would you like to play again (y to play again, anything else to quit)?: ")
        if play_again.lower() != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()