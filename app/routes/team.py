from flask_restful import Resource, reqparse
from flask import request, jsonify
from ..models.team_member import TeamMember
from ..db import db
from datetime import datetime

class TeamMemberListGet(Resource):
    def get(self):
        # Get query parameters
        department = request.args.get('department')
        featured = request.args.get('featured')
        public_only = request.args.get('public_only', 'true')
        
        query = TeamMember.query
        
        if department:
            query = query.filter(TeamMember.department == department)
        if featured == 'true':
            query = query.filter(TeamMember.is_featured == True)
        if public_only == 'true':
            query = query.filter(TeamMember.is_public == True)
            
        members = query.all()
        return jsonify([member.to_dict() for member in members])

class TeamMemberPost(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name is required')
        parser.add_argument('position', type=str, required=True, help='Position is required')
        parser.add_argument('department', type=str, required=True, help='Department is required')
        parser.add_argument('specialization', type=str, required=False)
        parser.add_argument('bio', type=str, required=True, help='Bio is required')
        parser.add_argument('education', type=list, location='json', required=False)
        parser.add_argument('experience_years', type=int, required=False)
        parser.add_argument('research_interests', type=list, location='json', required=False)
        parser.add_argument('publications', type=list, location='json', required=False)
        parser.add_argument('awards', type=list, location='json', required=False)
        parser.add_argument('profile_image', type=str, required=True, help='Profile image is required')
        parser.add_argument('gallery_images', type=list, location='json', required=False)
        parser.add_argument('email', type=str, required=False)
        parser.add_argument('phone', type=str, required=False)
        parser.add_argument('linkedin_url', type=str, required=False)
        parser.add_argument('orcid_id', type=str, required=False)
        parser.add_argument('languages_spoken', type=list, location='json', required=False)
        parser.add_argument('current_projects', type=list, location='json', required=False)
        parser.add_argument('join_date', type=str, required=False)
        parser.add_argument('is_public', type=bool, required=False)
        parser.add_argument('is_featured', type=bool, required=False)

        args = parser.parse_args()
        
        # Convert join_date string to date object
        if args.get('join_date'):
            args['join_date'] = datetime.strptime(args['join_date'], '%Y-%m-%d').date()
        
        member = TeamMember.create(**args)
        return jsonify(member.to_dict()), 201

class TeamMemberDetail(Resource):
    def get(self, id):
        member = TeamMember.query.get(id)
        if not member:
            return {"message": "Team member not found."}, 404
        return jsonify(member.to_dict())
    
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('position', type=str)
        parser.add_argument('department', type=str)
        parser.add_argument('specialization', type=str)
        parser.add_argument('bio', type=str)
        parser.add_argument('education', type=list, location='json')
        parser.add_argument('experience_years', type=int)
        parser.add_argument('research_interests', type=list, location='json')
        parser.add_argument('publications', type=list, location='json')
        parser.add_argument('awards', type=list, location='json')
        parser.add_argument('profile_image', type=str)
        parser.add_argument('gallery_images', type=list, location='json')
        parser.add_argument('email', type=str)
        parser.add_argument('phone', type=str)
        parser.add_argument('linkedin_url', type=str)
        parser.add_argument('orcid_id', type=str)
        parser.add_argument('languages_spoken', type=list, location='json')
        parser.add_argument('current_projects', type=list, location='json')
        parser.add_argument('join_date', type=str)
        parser.add_argument('is_public', type=bool)
        parser.add_argument('is_featured', type=bool)

        args = parser.parse_args()
        
        # Convert join_date string to date object if provided
        if args.get('join_date'):
            args['join_date'] = datetime.strptime(args['join_date'], '%Y-%m-%d').date()
        
        updated = TeamMember.update(id, **args)
        if not updated:
            return {"message": "Team member not found."}, 404

        return jsonify(updated.to_dict())

    def delete(self, id):
        deleted = TeamMember.delete_by_id(id)
        if not deleted:
            return {"message": "Team member not found."}, 404

        return {"message": f"Team member with id {id} deleted successfully."}, 200
