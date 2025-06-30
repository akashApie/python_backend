from flask import Blueprint
from flask_restful import Api
from .about import AboutUsGetAndPost,AboutUsUpdateDelete

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

def add_resources(app):
    app.add_resource(AboutUsGetAndPost,'/about')
    app.add_resource(AboutUsUpdateDelete,'/about/<int:id>')

def register_blueprints(app):
    app.register_blueprints(api_blueprint, url_prefix='api/v1')