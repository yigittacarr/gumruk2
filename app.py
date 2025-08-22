from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Merhaba!</h1><p>Bu benim ilk Python web sitem 🎉</p>"

if __name__ == "__main__":
    app.run(debug=True)
