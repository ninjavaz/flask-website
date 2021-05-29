from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello <h1>WORLD</h1>"



if __name__ == "__main__":
    app.run()