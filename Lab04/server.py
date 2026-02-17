from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()

    with open("cards.txt", "a") as f:
        f.write(str(data) + "\n")

    return jsonify({"status":"saved"})

app.run(port=8000)
