from flask_restful import Resource, reqparse
from flask import request, jsonify
from ..models.species import Species
from ..db import db

class SpeciesListGet(Resource):
    def get(self):
        # Get query parameters
        category = request.args.get('category')
        featured = request.args.get('featured')
        
        query = Species.query
        
        if category:
            query = query.filter(Species.category == category)
        if featured == 'true':
            query = query.filter(Species.is_featured == True)
            
        species_list = query.all()
        return jsonify([species.to_dict() for species in species_list])

class SpeciesPost(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name is required')
        parser.add_argument('scientific_name', type=str, required=True, help='Scientific name is required')
        parser.add_argument('category', type=str, required=True, help='Category is required')
        parser.add_argument('conservation_status', type=str, required=True, help='Conservation status is required')
        parser.add_argument('habitat', type=str, required=True, help='Habitat is required')
        parser.add_argument('description', type=str, required=True, help='Description is required')
        parser.add_argument('diet', type=str, required=True, help='Diet is required')
        parser.add_argument('size', type=str, required=True, help='Size is required')
        parser.add_argument('lifespan', type=str, required=True, help='Lifespan is required')
        parser.add_argument('main_image', type=str, required=True, help='Main image is required')
        parser.add_argument('distribution', type=str, required=True, help='Distribution is required')
        parser.add_argument('gallery_images', type=list, location='json', required=False)
        parser.add_argument('interesting_facts', type=list, location='json', required=False)
        parser.add_argument('breeding_info', type=str, required=False)
        parser.add_argument('threats', type=str, required=False)
        parser.add_argument('is_venomous', type=bool, required=False)
        parser.add_argument('is_featured', type=bool, required=False)

        args = parser.parse_args()
        
        species = Species.create(**args)
        return jsonify(species.to_dict()), 201

class SpeciesDetail(Resource):
    def get(self, id):
        species = Species.query.get(id)
        if not species:
            return {"message": "Species not found."}, 404
        return jsonify(species.to_dict())
    
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('scientific_name', type=str)
        parser.add_argument('category', type=str)
        parser.add_argument('conservation_status', type=str)
        parser.add_argument('habitat', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('diet', type=str)
        parser.add_argument('size', type=str)
        parser.add_argument('lifespan', type=str)
        parser.add_argument('main_image', type=str)
        parser.add_argument('distribution', type=str)
        parser.add_argument('gallery_images', type=list, location='json')
        parser.add_argument('interesting_facts', type=list, location='json')
        parser.add_argument('breeding_info', type=str)
        parser.add_argument('threats', type=str)
        parser.add_argument('is_venomous', type=bool)
        parser.add_argument('is_featured', type=bool)

        args = parser.parse_args()
        
        updated = Species.update(id, **args)
        if not updated:
            return {"message": "Species not found."}, 404

        return jsonify(updated.to_dict())

    def delete(self, id):
        deleted = Species.delete_by_id(id)
        if not deleted:
            return {"message": "Species not found."}, 404

        return {"message": f"Species with id {id} deleted successfully."}, 200
