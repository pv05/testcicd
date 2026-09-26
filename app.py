import os

from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "default-app786")
GREETING = os.getenv("GREETING", "Hello")

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(message=f"{GREETING} from {APP_NAME}!")


@app.route("/health")
def health():
    return jsonify(status="ok", app=APP_NAME)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
