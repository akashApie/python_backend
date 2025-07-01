from flask import Flask,jsonify
from flask_cors import CORS
from app.config import config

from .db import db
from .routes import add_resources, register_blueprints

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    CORS(app, resources = {
        r"/api/*":{
            "origins": app.config.get('CORS_ORIGINS', '*'),
            "supports_credentials": True
        }
    })

    with app.app_context():
        db.create_all()
    
    add_resources()
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