from flask import Flask
from flask_cors import CORS
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Enable CORS
    CORS(app)
    
    # Register blueprints
    from app.routes.ai_routes import ai_bp
    app.register_blueprint(ai_bp)
    
    @app.route('/')
    def home():
        return {"message": "Welcome to the Flask API"}
    
    return app
