from firebase_functions import https_fn
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Firebase Cloud Functions with Python'

@https_fn.on_request(max_instances=1)
def articles(req: https_fn.Request) -> https_fn.Response:
    with app.request_context(req.environ):
        return app.full_dispatch_request()