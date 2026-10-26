import random


def get_guess():
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            return guess
        except ValueError:
            print("That's not a valid number! Try again....🥹")
def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = get_guess()
        attempts += 1
            
        if guess == secret_number:
            print("correct....🙂")
            break
        elif guess > secret_number:
            print("Too high")
        elif guess < secret_number:
            print("Too low")

        if attempts == 7:
            print(f"You've used all your attempts! Game over. The number was {secret_number}")
            break
        print("Attempts:", attempts)
while True:
    play_game()
    again = input("Play again?? (y/n): ")
    if again != "y":
        break
