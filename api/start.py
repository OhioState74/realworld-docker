from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    a = os.environ.get('a12', 'codeorion')
    return f"Hello World!@!2222 {a}"


if __name__ == "__main__":
    app.run()
