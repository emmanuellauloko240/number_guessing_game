import random

secret_number = random.randint(1, 100)
attempts = 0
while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
    except ValueError:
        print("That's not a valid number! Try again....🥹")
        continue

    if guess == secret_number:
        print("correct....🙂")
        break
    elif guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")

    if attempts == 7:
        print("You've used all your attempts! Game over.")
        break
    print("Attempts:", attempts)
