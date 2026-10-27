import random
from flask import Flask, render_template, request,session
app = Flask(__name__)
app.secret_key = "dev-key-change-later"
@app.route("/guess-game", methods=["GET","POST"])

def music_home():
    
    if "secret_number" not in session:
        session["secret_number"] = random.randint(1, 100)
    if request.method == "POST":
        secret_number = session["secret_number"]
        guess = int(request.form["guess"])
        guess = int(request.form["action"])
        message = ""
        if guess < secret_number:
            message = "Too low!🫣"
        elif guess > secret_number:
            message = "Too high🤓"
        else:
            message = "Correct🥳"
            session.pop("secret_number", None)
        return render_template("index.html",guess = guess, message=message)

    return render_template("index.html", guess="")
