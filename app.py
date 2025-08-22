import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Merhaba Render!</h1><p>Python Flask web sitem yayında 🎉</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render'ın verdiği PORT
    app.run(host="0.0.0.0", port=port)        # Tüm ağ arayüzlerinden dinle

