import time

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/ping")
def ping():
    start = time.perf_counter()
    response = {"message": "pong"}
    response["response_time_ms"] = round((time.perf_counter() - start) * 1000, 3)
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
