from flask import Flask, request, jsonify
from password_checker import analyze_password

app = Flask(__name__)

@app.route("/")
def home():
    return "API password checker OK"

@app.route("/check-password", methods=["POST"])
def check_password():

    data = request.get_json()
    password = data.get("password", "")

    return jsonify(analyze_password(password))


if __name__ == "__main__":
    app.run(debug=True)