from flask import Flask, request, jsonify
from password_checker import analyze_password

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Password Checker</h1>
    <input id="pwd" type="text" placeholder="mot de passe">
    <button onclick="send()">Tester</button>
    <pre id="result"></pre>

    <script>
    async function send() {
        const password = document.getElementById("pwd").value;

        const res = await fetch("/check-password", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({password})
        });

        const data = await res.json();
        document.getElementById("result").innerText =
            JSON.stringify(data, null, 2);
    }
    </script>
    """

@app.route("/check-password", methods=["POST"])
def check_password():

    data = request.get_json()
    password = data.get("password", "")

    return jsonify(analyze_password(password))


if __name__ == "__main__":
    app.run(debug=True)