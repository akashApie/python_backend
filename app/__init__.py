from flask import Flask
from .models import db
from flask_cors import CORS
from config import config
from .routes import add_resources, register_blueprints

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    CORS(app, resources = {
        r"/api/*":{
            "origins": app.config.get('CORS_ORIGINS','*'),
            "supports_credentials": True
        }
    })

    with app.app_context():
        db.create_all()

    add_resources(app)
    register_blueprints(app)

    register_error_handlers(app)

    return app

def register_error_handlers(app):
    from werkzeug.exceptions import HTTPException

    @app.errorhandler(HTTPException)
    def handle_http_error(error):
        return jsonify({
            'error': {
                'code': error.code,
                'message': error.description
            }
        }), error.code