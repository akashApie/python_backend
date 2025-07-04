from flask_restful import Resource, reqparse
from flask import request, jsonify
from ..models.slide import Slide
from ..db import db
from datetime import datetime

class SlideListGet(Resource):
    def get(self):
        # Get query parameters
        category = request.args.get('category')
        active_only = request.args.get('active_only', 'true')
        
        query = Slide.query
        
        if category:
            query = query.filter(Slide.category == category)
        if active_only == 'true':
            query = query.filter(Slide.is_active == True)
            
        slides = query.order_by(Slide.order_position.asc()).all()
        return jsonify([slide.to_dict() for slide in slides])

class SlidePost(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='Title is required')
        parser.add_argument('subtitle', type=str, required=False)
        parser.add_argument('description', type=str, required=False)
        parser.add_argument('image_url', type=str, required=True, help='Image URL is required')
        parser.add_argument('background_image', type=str, required=False)
        parser.add_argument('call_to_action_text', type=str, required=False)
        parser.add_argument('call_to_action_url', type=str, required=False)
        parser.add_argument('order_position', type=int, required=False)
        parser.add_argument('category', type=str, required=True, help='Category is required')
        parser.add_argument('is_active', type=bool, required=False)
        parser.add_argument('start_date', type=str, required=False)
        parser.add_argument('end_date', type=str, required=False)
        parser.add_argument('overlay_color', type=str, required=False)
        parser.add_argument('text_color', type=str, required=False)
        parser.add_argument('animation_type', type=str, required=False)
        parser.add_argument('display_duration', type=int, required=False)

        args = parser.parse_args()
        
        # Convert date strings to date objects
        if args.get('start_date'):
            args['start_date'] = datetime.strptime(args['start_date'], '%Y-%m-%d').date()
        if args.get('end_date'):
            args['end_date'] = datetime.strptime(args['end_date'], '%Y-%m-%d').date()
        
        slide = Slide.create(**args)
        return jsonify(slide.to_dict()), 201

class SlideDetail(Resource):
    def get(self, id):
        slide = Slide.query.get(id)
        if not slide:
            return {"message": "Slide not found."}, 404
        return jsonify(slide.to_dict())
    
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('subtitle', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('image_url', type=str)
        parser.add_argument('background_image', type=str)
        parser.add_argument('call_to_action_text', type=str)
        parser.add_argument('call_to_action_url', type=str)
        parser.add_argument('order_position', type=int)
        parser.add_argument('category', type=str)
        parser.add_argument('is_active', type=bool)
        parser.add_argument('start_date', type=str)
        parser.add_argument('end_date', type=str)
        parser.add_argument('overlay_color', type=str)
        parser.add_argument('text_color', type=str)
        parser.add_argument('animation_type', type=str)
        parser.add_argument('display_duration', type=int)

        args = parser.parse_args()
        
        # Convert date strings to date objects if provided
        if args.get('start_date'):
            args['start_date'] = datetime.strptime(args['start_date'], '%Y-%m-%d').date()
        if args.get('end_date'):
            args['end_date'] = datetime.strptime(args['end_date'], '%Y-%m-%d').date()
        
        updated = Slide.update(id, **args)
        if not updated:
            return {"message": "Slide not found."}, 404

        return jsonify(updated.to_dict())

    def delete(self, id):
        deleted = Slide.delete_by_id(id)
        if not deleted:
            return {"message": "Slide not found."}, 404

        return {"message": f"Slide with id {id} deleted successfully."}, 200
