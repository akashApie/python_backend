from flask_restful import Resource, reqparse
from flask import request, jsonify
from ..models.conservation_project import ConservationProject
from ..db import db
from datetime import datetime

class ConservationProjectListGet(Resource):
    def get(self):
        # Get query parameters
        category = request.args.get('category')
        status = request.args.get('status')
        featured = request.args.get('featured')
        
        query = ConservationProject.query
        
        if category:
            query = query.filter(ConservationProject.category == category)
        if status:
            query = query.filter(ConservationProject.status == status)
        if featured == 'true':
            query = query.filter(ConservationProject.is_featured == True)
            
        projects = query.all()
        return jsonify([project.to_dict() for project in projects])

class ConservationProjectPost(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='Title is required')
        parser.add_argument('subtitle', type=str, required=False)
        parser.add_argument('category', type=str, required=True, help='Category is required')
        parser.add_argument('status', type=str, required=True, help='Status is required')
        parser.add_argument('start_date', type=str, required=False)
        parser.add_argument('end_date', type=str, required=False)
        parser.add_argument('location', type=str, required=True, help='Location is required')
        parser.add_argument('description', type=str, required=True, help='Description is required')
        parser.add_argument('objectives', type=list, location='json', required=True, help='Objectives are required')
        parser.add_argument('methodology', type=str, required=False)
        parser.add_argument('results', type=str, required=False)
        parser.add_argument('impact', type=str, required=False)
        parser.add_argument('main_image', type=str, required=True, help='Main image is required')
        parser.add_argument('gallery_images', type=list, location='json', required=False)
        parser.add_argument('species_involved', type=list, location='json', required=False)
        parser.add_argument('partners', type=list, location='json', required=False)
        parser.add_argument('funding_sources', type=list, location='json', required=False)
        parser.add_argument('budget', type=str, required=False)
        parser.add_argument('lead_researcher', type=str, required=False)
        parser.add_argument('publications', type=list, location='json', required=False)
        parser.add_argument('is_featured', type=bool, required=False)

        args = parser.parse_args()
        
        # Convert date strings to date objects
        if args.get('start_date'):
            args['start_date'] = datetime.strptime(args['start_date'], '%Y-%m-%d').date()
        if args.get('end_date'):
            args['end_date'] = datetime.strptime(args['end_date'], '%Y-%m-%d').date()
        
        project = ConservationProject.create(**args)
        return jsonify(project.to_dict()), 201

class ConservationProjectDetail(Resource):
    def get(self, id):
        project = ConservationProject.query.get(id)
        if not project:
            return {"message": "Conservation project not found."}, 404
        return jsonify(project.to_dict())
    
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('subtitle', type=str)
        parser.add_argument('category', type=str)
        parser.add_argument('status', type=str)
        parser.add_argument('start_date', type=str)
        parser.add_argument('end_date', type=str)
        parser.add_argument('location', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('objectives', type=list, location='json')
        parser.add_argument('methodology', type=str)
        parser.add_argument('results', type=str)
        parser.add_argument('impact', type=str)
        parser.add_argument('main_image', type=str)
        parser.add_argument('gallery_images', type=list, location='json')
        parser.add_argument('species_involved', type=list, location='json')
        parser.add_argument('partners', type=list, location='json')
        parser.add_argument('funding_sources', type=list, location='json')
        parser.add_argument('budget', type=str)
        parser.add_argument('lead_researcher', type=str)
        parser.add_argument('publications', type=list, location='json')
        parser.add_argument('is_featured', type=bool)

        args = parser.parse_args()
        
        # Convert date strings to date objects
        if args.get('start_date'):
            args['start_date'] = datetime.strptime(args['start_date'], '%Y-%m-%d').date()
        if args.get('end_date'):
            args['end_date'] = datetime.strptime(args['end_date'], '%Y-%m-%d').date()
        
        updated = ConservationProject.update(id, **args)
        if not updated:
            return {"message": "Conservation project not found."}, 404

        return jsonify(updated.to_dict())

    def delete(self, id):
        deleted = ConservationProject.delete_by_id(id)
        if not deleted:
            return {"message": "Conservation project not found."}, 404

        return {"message": f"Conservation project with id {id} deleted successfully."}, 200
