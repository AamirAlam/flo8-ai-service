from flask import Flask
from flask_cors import CORS
from app.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Enable CORS with specific settings
    CORS(app, resources={
        r"/*": {
            "origins": "*",  # Allow all origins, change to specific domains in production
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization", "X-Custom-Header"],
            "expose_headers": ["Content-Length"],
            "supports_credentials": True,  # Allow cookies in cross-origin requests
            "max_age": 86400  # Cache preflight response for 24 hours
        }
    })
    
    # Register blueprints
    from app.routes.ai_routes import ai_bp
    app.register_blueprint(ai_bp)
    
    @app.route('/')
    def home():
        return {"message": "Welcome to the Flask API with AI integration!"}
    
    return app
