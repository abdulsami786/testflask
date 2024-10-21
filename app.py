from flask import Flask, request, jsonify




app = Flask(__name__)


@app.route("/")
def hello() -> str:
    """Return a friendly HTTP greeting.

    Returns:
        A string with the words 'Hello World!'.
    """
    return "Hello World!"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)