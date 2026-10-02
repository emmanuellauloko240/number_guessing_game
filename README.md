# Number Guessing Game

A simple command-line Python game where the player tries to guess a randomly generated number between 1 and 100, with limited attempts and helpful hints.

## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository:
```bash
   git clone https://github.com/emmanuellaenenu/number-guessing-game.git
```
3. Navigate into the project folder:
```bash
   cd number-guessing-game
```
4. Run the game:
```bash
   python3 game.py
```

## Features

- Randomly generated secret number between 1 and 100
- Unlimited guesses with hints ("Too high" / "Too low")
- Limited to 7 attempts per round
- Reveals the secret number if you run out of attempts
- Handles invalid input gracefully (no crashes)
- Option to play again after each round

## What I Learned

Building this project helped me understand:

- Variables and how they store and update data
- Functions, including defining them, calling them, and using `return`
- Variable scope (why variables inside a function don't exist outside it)
- Loops (`while`) and how to control them with `break` and `continue`
- Handling errors gracefully with `try`/`except`
- Formatting strings with f-strings
- Using Git and GitHub to track and share my code