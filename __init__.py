from flask import Flask
from app.firebase_config import initialize_firebase

db = initialize_firebase()

def create_app():
    app = Flask(__name__)
    
    from app.routes import api_bp
    app.register_blueprint(api_bp)

    return app