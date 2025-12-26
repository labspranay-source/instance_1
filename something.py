from flask import Flask

app = Flask(__name__)

@app.route("/nothing")
def home():
    return "Hello! This is a simple Python web service."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)