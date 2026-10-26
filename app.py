from flask import Flask, render_template
app = Flask(__name__)
@app.route("/guess-game")

def music_home():
    return "Welcome to my Number-guessing-game"