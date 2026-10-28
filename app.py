import random
from flask import Flask, render_template, request,session
app = Flask(__name__)
app.secret_key = "dev-key-change-later"
@app.route("/guess-game", methods=["GET","POST"])

# def music_home():
    
#     if "secret_number" not in session:
#         session["secret_number"] = random.randint(1, 100)
#     if "guess_count" not in session:
#         session["guess_count"] = 0
#     if "game_over🥱" not in session:
#         session["game_over🥱"] = False
#     if request.method == "POST":
#         if request.form.get("action") == "restart":
#             session["secret_number"] = random.randint(1, 100)
#             session["guess_count"] = 0
#             if session["game_over🥱"] == True:
#                 return render_template("index.html", guess="", guess_count=session["guess_count"], message="Game over! Click Play Again🎮")
#         else:
#             if session["game_over🥱"] == True:
#                 return render_template("index.html", guess="", guess_count=session["guess_count"], message="Game over! Click Play Again🎮")
#             else:
#             # secret_number = session["secret_number"]
#                 session["guess_count"] += 1
#                 guess = int(request.form["guess"])
#                 message = ""
#             if guess == secret_number:
#                 message = "Correct🥳"
#                 session["game_over🥱"] = True 
#             elif session["guess_count"] == 7:
#                 message = f"You used {session['guess_count']} attempts and the secret_number is {secret_number} 😌!!!"
#                 session["game_over🥱"]
#             elif guess < secret_number:
#                 message = "Too low"
#             elif guess > secret_number:
#                 message = "Too high🤓"
#             return render_template("index.html",
#             guess = guess, message=message,
#              guess_count=session["guess_count"])



def music_home():

    if "secret_number" not in session:
        session["secret_number"] = random.randint(1, 100)

    if "guess_count" not in session:
        session["guess_count"] = 0

    if "game_over🥱" not in session:
        session["game_over🥱"] = False

    if request.method == "POST":

        # Handle restart
        if request.form.get("action") == "restart":
            session["secret_number"] = random.randint(1, 100)
            session["guess_count"] = 0
            session["game_over🥱"] = False  # ADDED: reset game-over state

        else:
            if session["game_over🥱"]:
                return render_template(
                    "index.html",
                    guess="",
                    guess_count=session["guess_count"],
                    message="Game over! Click Play Again 🎮"
                )

            secret_number = session["secret_number"]  # RESTORED

            session["guess_count"] += 1
            guess = int(request.form["guess"])
            message = ""

            if guess == secret_number:
                message = "Correct🥳"
                session["game_over🥱"] = True

            elif session["guess_count"] == 7:
                message = (
                    f"You used {session['guess_count']} attempts "
                    f"and the secret number is {secret_number} 😌!!!"
                )
                session["game_over🥱"] = True  # CORRECTED: assign True

            elif guess < secret_number:
                message = "Too low"

            else:
                message = "Too high🤓"

            return render_template(
                "index.html",
                guess=guess,
                message=message,
                guess_count=session["guess_count"]
            )

    # ADDED: handles GET requests and displays the page after restart
    return render_template(
        "index.html",
        guess="",
        guess_count=session["guess_count"]
    )
