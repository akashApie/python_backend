from flask_restful import Resource, reqparse
from flask import request, jsonify
from ..models.aboutus import AboutUs
from ..db import db

class AboutUsGet(Resource):
    def get(self):
        about_sections= AboutUs.query.all()
        return jsonify([section.to_dict() for section in about_sections])

class AboutUsPost(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='Title is required')
        parser.add_argument('subtitle', type=str, required=False)
        parser.add_argument('section_type', type=str, required=True, help='Section type is required')
        parser.add_argument('text', type=str, required=True, help='Text is required')
        parser.add_argument('image', type=str, required=True, help='Image is required')
        parser.add_argument('information', type=str, required=True, help='Information is required')
        parser.add_argument('additional_information', type=str, required=True, help='Additional information is required')
        parser.add_argument('additional_images', type=list, location='json', required=False)
        parser.add_argument('subsections', type=list, location='json', required=False)
        parser.add_argument('key_points', type=list, location='json', required=False)
        parser.add_argument('timeline_data', type=list, location='json', required=False)
        parser.add_argument('statistics', type=dict, location='json', required=False)
        parser.add_argument('quotes', type=list, location='json', required=False)
        parser.add_argument('order_position', type=int, required=False)
        parser.add_argument('is_featured', type=bool, required=False)
        parser.add_argument('is_published', type=bool, required=False)

        args = parser.parse_args()

        about = AboutUs.create(**args)
        return jsonify(about.to_dict()), 201

class AboutUsUpdate(Resource):
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('subtitle', type=str)
        parser.add_argument('section_type', type=str)
        parser.add_argument('text', type=str)
        parser.add_argument('image', type=str)
        parser.add_argument('information', type=str)
        parser.add_argument('additional_information', type=str)
        parser.add_argument('additional_images', type=list, location='json')
        parser.add_argument('subsections', type=list, location='json')
        parser.add_argument('key_points', type=list, location='json')
        parser.add_argument('timeline_data', type=list, location='json')
        parser.add_argument('statistics', type=dict, location='json')
        parser.add_argument('quotes', type=list, location='json')
        parser.add_argument('order_position', type=int)
        parser.add_argument('is_featured', type=bool)
        parser.add_argument('is_published', type=bool)

        args = parser.parse_args()

        updated = AboutUs.update(id, **args)

        if not updated:
            return {"message": "AboutUs entry not found."}, 404

        return jsonify(updated.to_dict())

class AboutUsDelete(Resource):
    def delete(self, id):
        deleted = AboutUs.delete_by_id(id)

        if not deleted:
            return {"message": "AboutUs entry not found."}, 404

        return {"message": f"AboutUs entry with id {id} deleted successfully."}, 200
