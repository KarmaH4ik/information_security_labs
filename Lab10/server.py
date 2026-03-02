from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/")
def api():
    return jsonify({"message": "Hello from API!"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
