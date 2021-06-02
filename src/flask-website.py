from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello <h1>WORLD</h1>"

if __name__ == "__main__":
    app.run()