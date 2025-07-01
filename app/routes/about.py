from flask_restful import Resource, reqparse
from flask import request, jsonify
from ..models.aboutus import AboutUs
from .. import db

class AboutUsGet(Resource):
    def get(self):
        about_sections= AboutUs.query.all()
        return jsonify([section.to_dict() for section in about_sections])

class AboutUsPost(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='Title is required')
        parser.add_argument('text', type=str, required=True, help='Text is required')
        parser.add_argument('image', type=str, required=True, help='Image is required')
        parser.add_argument('information', type=str, required=True, help='Information is required')
        parser.add_argument('additional_information', type=str, required=True, help='Additional information is required')
        parser.add_argument('additional_images', type=list, location='json', required=False)  # Optional list

        args = parser.parse_args()

        about = AboutUs.create(
            title=args['title'],
            text=args['text'],
            image=args['image'],
            information=args['information'],
            additional_information=args['additional_information'],
            additional_images=args.get('additional_images', [])
        )

        return jsonify(about.to_dict()), 201

class AboutUsUpdate(Resource):
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('text', type=str)
        parser.add_argument('image', type=str)
        parser.add_argument('information', type=str)
        parser.add_argument('additional_information', type=str)
        parser.add_argument('additional_images', type=list, location='json')

        args = parser.parse_args()

        updated = AboutUs.update(
            id,
            title=args.get('title'),
            text=args.get('text'),
            image=args.get('image'),
            information=args.get('information'),
            additional_information=args.get('additional_information'),
            additional_images=args.get('additional_images')
        )

        if not updated:
            return {"message": "AboutUs entry not found."}, 404

        return jsonify(updated.to_dict())

class AboutUsDelete(Resource):
    def delete(self, id):
        deleted = AboutUs.delete_by_id(id)

        if not deleted:
            return {"message": "AboutUs entry not found."}, 404

        return {"message": f"AboutUs entry with id {id} deleted successfully."}, 200
