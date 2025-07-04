from flask import Blueprint
from flask_restful import Api
from .about import AboutUsGet, AboutUsUpdate, AboutUsPost, AboutUsDelete
from .species import SpeciesListGet, SpeciesPost, SpeciesDetail
from .conservation import ConservationProjectListGet, ConservationProjectPost, ConservationProjectDetail
from .events import EventListGet, EventPost, EventDetail
from .team import TeamMemberListGet, TeamMemberPost, TeamMemberDetail
from .slides import SlideListGet, SlidePost, SlideDetail
from .pages import PageListGet, PagePost, PageDetail, PageBySlugDetail

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

def add_resources():
    # About Us routes
    api.add_resource(AboutUsGet, '/about')
    api.add_resource(AboutUsPost, '/about')
    api.add_resource(AboutUsUpdate, '/about/<int:id>')
    api.add_resource(AboutUsDelete, '/about/<int:id>')
    
    # Species routes
    api.add_resource(SpeciesListGet, '/species')
    api.add_resource(SpeciesPost, '/species')
    api.add_resource(SpeciesDetail, '/species/<int:id>')
    
    # Conservation Project routes
    api.add_resource(ConservationProjectListGet, '/conservation')
    api.add_resource(ConservationProjectPost, '/conservation')
    api.add_resource(ConservationProjectDetail, '/conservation/<int:id>')
    
    # Event routes
    api.add_resource(EventListGet, '/events')
    api.add_resource(EventPost, '/events')
    api.add_resource(EventDetail, '/events/<int:id>')
    
    # Team Member routes
    api.add_resource(TeamMemberListGet, '/team')
    api.add_resource(TeamMemberPost, '/team')
    api.add_resource(TeamMemberDetail, '/team/<int:id>')
    
    # Slide routes
    api.add_resource(SlideListGet, '/slides')
    api.add_resource(SlidePost, '/slides')
    api.add_resource(SlideDetail, '/slides/<int:id>')
    
    # Page routes
    api.add_resource(PageListGet, '/pages')
    api.add_resource(PagePost, '/pages')
    api.add_resource(PageDetail, '/pages/<int:id>')
    api.add_resource(PageBySlugDetail, '/pages/slug/<string:slug>')

def register_blueprints(app):
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')