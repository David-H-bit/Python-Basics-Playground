def quiz_game():

    questions = (
                "Q1. What is the capital city of France?",
                "Q2. Which data type is immutable in Python?",
                "Q3. Who wrote the play 'Romeo and Juliet'?",
                "Q4. What is the largest planet in our Solar System?",
                "Q5. Which operator is used for exponentiation in Python?"
                )

    options = (
                ("a) Rome", "b) Madrid", "c) Paris", "d) Berlin"),
                ("a) List", "b) Dictionary", "c) String", "d) Set"), 
                ("a) William Shakespeare", "b) Charles Dickens", "c) Mark Twain", "d) Jane Austen"), 
                ("a) Earth", "b) Saturn", "c) Jupiter", "d) Neptune"), 
                ("a) ^", "b) **", "c) //", "d) %")
                )

    answers = ["c", "c", "a", "c", "b"]
    guesses = []
    question_num = 0
    correct_answers = 0

    print("------------QUIZ------------")
    print("Guess the right answers (a, b, c or d)")
    print("")

    for question in questions:
        print(question)
        for option in options[question_num]:
            print(option)
        
        while True:
            print("")
            guess = input("Enter your answer (a, b, c, d): ").lower()
            if guess not in ["a", "b", "c", "d"]:
                print("only enter one of the four options please (a, b, c or d)")
            else:
                if guess == answers[question_num]:
                    print("")
                    print("Correct!")
                    print("")
                    guesses.append(guess)
                    correct_answers += 1
                else:
                    print("") 
                    print(f"not correct, the answer was {answers[question_num]}")
                    print("")
                    guesses.append(guess)
                break

        question_num+= 1

    print("---------|--------|---------")
    print("---------| RESULT |---------")
    print("---------|--------|---------")
    print("")
    print((f"You got a score of {correct_answers}/{len(answers)}"))
    print(f"the answers: {answers}")
    print(f"your guesses: {guesses}")
    print("")

    if correct_answers == len(answers):
        print("🏆 Perfect score! Amazing job!")
        print("")
    elif correct_answers / len(answers) >= 0.6:
        print("👍 Good work, you know your stuff!")
        print("")
    else:
        print("📘 Keep practicing, you’ll get there!")
        print("")

    print("----------------------------")
    print("")
    play_again = input("Type 'Y' to play again: ")
    if play_again.upper() == "Y":
        quiz_game()

quiz_game()
print("-----THANKS FOR PLAYING!----")

        