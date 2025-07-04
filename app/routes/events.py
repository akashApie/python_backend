from flask_restful import Resource, reqparse
from flask import request, jsonify
from ..models.event import Event
from ..db import db
from datetime import datetime

class EventListGet(Resource):
    def get(self):
        # Get query parameters
        category = request.args.get('category')
        event_type = request.args.get('event_type')
        featured = request.args.get('featured')
        upcoming = request.args.get('upcoming')
        
        query = Event.query
        
        if category:
            query = query.filter(Event.category == category)
        if event_type:
            query = query.filter(Event.event_type == event_type)
        if featured == 'true':
            query = query.filter(Event.is_featured == True)
        if upcoming == 'true':
            query = query.filter(Event.start_datetime > datetime.now())
            
        events = query.order_by(Event.start_datetime.asc()).all()
        return jsonify([event.to_dict() for event in events])

class EventPost(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='Title is required')
        parser.add_argument('subtitle', type=str, required=False)
        parser.add_argument('category', type=str, required=True, help='Category is required')
        parser.add_argument('event_type', type=str, required=True, help='Event type is required')
        parser.add_argument('start_datetime', type=str, required=True, help='Start datetime is required')
        parser.add_argument('end_datetime', type=str, required=True, help='End datetime is required')
        parser.add_argument('location', type=str, required=True, help='Location is required')
        parser.add_argument('venue_details', type=str, required=False)
        parser.add_argument('description', type=str, required=True, help='Description is required')
        parser.add_argument('detailed_agenda', type=str, required=False)
        parser.add_argument('target_audience', type=str, required=True, help='Target audience is required')
        parser.add_argument('max_participants', type=int, required=False)
        parser.add_argument('registration_fee', type=float, required=False)
        parser.add_argument('prerequisites', type=str, required=False)
        parser.add_argument('what_to_bring', type=list, location='json', required=False)
        parser.add_argument('main_image', type=str, required=True, help='Main image is required')
        parser.add_argument('gallery_images', type=list, location='json', required=False)
        parser.add_argument('organizers', type=list, location='json', required=False)
        parser.add_argument('guest_speakers', type=list, location='json', required=False)
        parser.add_argument('registration_link', type=str, required=False)
        parser.add_argument('contact_person', type=str, required=False)
        parser.add_argument('contact_email', type=str, required=False)
        parser.add_argument('contact_phone', type=str, required=False)
        parser.add_argument('is_featured', type=bool, required=False)

        args = parser.parse_args()
        
        # Convert datetime strings to datetime objects
        args['start_datetime'] = datetime.fromisoformat(args['start_datetime'])
        args['end_datetime'] = datetime.fromisoformat(args['end_datetime'])
        
        event = Event.create(**args)
        return jsonify(event.to_dict()), 201

class EventDetail(Resource):
    def get(self, id):
        event = Event.query.get(id)
        if not event:
            return {"message": "Event not found."}, 404
        return jsonify(event.to_dict())
    
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('subtitle', type=str)
        parser.add_argument('category', type=str)
        parser.add_argument('event_type', type=str)
        parser.add_argument('start_datetime', type=str)
        parser.add_argument('end_datetime', type=str)
        parser.add_argument('location', type=str)
        parser.add_argument('venue_details', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('detailed_agenda', type=str)
        parser.add_argument('target_audience', type=str)
        parser.add_argument('max_participants', type=int)
        parser.add_argument('current_registrations', type=int)
        parser.add_argument('registration_fee', type=float)
        parser.add_argument('prerequisites', type=str)
        parser.add_argument('what_to_bring', type=list, location='json')
        parser.add_argument('main_image', type=str)
        parser.add_argument('gallery_images', type=list, location='json')
        parser.add_argument('organizers', type=list, location='json')
        parser.add_argument('guest_speakers', type=list, location='json')
        parser.add_argument('registration_link', type=str)
        parser.add_argument('contact_person', type=str)
        parser.add_argument('contact_email', type=str)
        parser.add_argument('contact_phone', type=str)
        parser.add_argument('is_featured', type=bool)
        parser.add_argument('is_cancelled', type=bool)
        parser.add_argument('cancellation_reason', type=str)

        args = parser.parse_args()
        
        # Convert datetime strings to datetime objects if provided
        if args.get('start_datetime'):
            args['start_datetime'] = datetime.fromisoformat(args['start_datetime'])
        if args.get('end_datetime'):
            args['end_datetime'] = datetime.fromisoformat(args['end_datetime'])
        
        updated = Event.update(id, **args)
        if not updated:
            return {"message": "Event not found."}, 404

        return jsonify(updated.to_dict())

    def delete(self, id):
        deleted = Event.delete_by_id(id)
        if not deleted:
            return {"message": "Event not found."}, 404

        return {"message": f"Event with id {id} deleted successfully."}, 200
