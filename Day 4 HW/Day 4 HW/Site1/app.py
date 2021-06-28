import os
from flask import Flask
app = Flask(__name__)
color = os.environ.get('COLOR')
@app.route("/")
def main():
    return "Container Site #1 is up and Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
