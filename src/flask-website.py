from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello <h1>WORLD</h1>"

@app.route("/<name>")
def name(name):
    return f"Name: {name}"




if __name__ == "__main__":
    app.run()