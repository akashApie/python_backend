from flask import Blueprint
from flask_restful import Api
from .about import AboutUsGet,AboutUsUpdate, AboutUsPost,AboutUsDelete

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

def add_resources():
    api.add_resource(AboutUsGet,'/about')
    api.add_resource(AboutUsUpdate,'/about/<int:id>')
    api.add_resource(AboutUsPost,'/about')
    api.add_resource(AboutUsDelete,'/about/<int:id>')

def register_blueprints(app):
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')