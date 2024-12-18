from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



#Function to check users' guess against actual answer 

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"You got it! The answer is {actual_answer}.")

#Function to set difficulty
def set_difficulty():
    level = input("Choose the difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Choose the level you want to play which is 'easy' or hard'")

def game():
    #Choose the random number between 1 and 100

    print(logo)

    print("Welcome to the Number Guessing Game!")

    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    print(f"Psst! The correct answer is {answer}.")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        #Let the user guess a number
        print(f"You have {turns} attempts remaining to guess the numbers.")
        guess = int(input("Guess the number: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose. Try Again!")
            return
        elif guess != answer:
            print("Guess again!")
game()

#Track the number of turns and reduce by 1 if they get it wrong

#Repeat the guessing functionality if they are wrong

