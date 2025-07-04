from flask_restful import Resource, reqparse
from flask import request, jsonify
from ..models.page import Page
from ..db import db
from datetime import datetime

class PageListGet(Resource):
    def get(self):
        # Get query parameters
        page_type = request.args.get('page_type')
        published_only = request.args.get('published_only', 'true')
        featured = request.args.get('featured')
        parent_id = request.args.get('parent_id')
        
        query = Page.query
        
        if page_type:
            query = query.filter(Page.page_type == page_type)
        if published_only == 'true':
            query = query.filter(Page.is_published == True)
        if featured == 'true':
            query = query.filter(Page.is_featured == True)
        if parent_id:
            query = query.filter(Page.parent_page_id == parent_id)
        else:
            # Default to top-level pages
            query = query.filter(Page.parent_page_id.is_(None))
            
        pages = query.order_by(Page.order_position.asc()).all()
        return jsonify([page.to_dict() for page in pages])

class PagePost(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='Title is required')
        parser.add_argument('slug', type=str, required=True, help='Slug is required')
        parser.add_argument('page_type', type=str, required=True, help='Page type is required')
        parser.add_argument('content', type=str, required=True, help='Content is required')
        parser.add_argument('meta_description', type=str, required=False)
        parser.add_argument('meta_keywords', type=list, location='json', required=False)
        parser.add_argument('main_image', type=str, required=False)
        parser.add_argument('gallery_images', type=list, location='json', required=False)
        parser.add_argument('sections', type=list, location='json', required=False)
        parser.add_argument('sidebar_content', type=str, required=False)
        parser.add_argument('is_published', type=bool, required=False)
        parser.add_argument('is_featured', type=bool, required=False)
        parser.add_argument('author', type=str, required=False)
        parser.add_argument('publish_date', type=str, required=False)
        parser.add_argument('parent_page_id', type=int, required=False)
        parser.add_argument('order_position', type=int, required=False)
        parser.add_argument('template_name', type=str, required=False)

        args = parser.parse_args()
        
        # Convert publish_date string to date object
        if args.get('publish_date'):
            args['publish_date'] = datetime.strptime(args['publish_date'], '%Y-%m-%d').date()
        
        page = Page.create(**args)
        return jsonify(page.to_dict()), 201

class PageDetail(Resource):
    def get(self, id=None, slug=None):
        if id:
            page = Page.query.get(id)
        elif slug:
            page = Page.query.filter_by(slug=slug).first()
        else:
            return {"message": "Page ID or slug is required."}, 400
            
        if not page:
            return {"message": "Page not found."}, 404
        
        # Increment view count
        page.view_count += 1
        page.save()
        
        return jsonify(page.to_dict())
    
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('slug', type=str)
        parser.add_argument('page_type', type=str)
        parser.add_argument('content', type=str)
        parser.add_argument('meta_description', type=str)
        parser.add_argument('meta_keywords', type=list, location='json')
        parser.add_argument('main_image', type=str)
        parser.add_argument('gallery_images', type=list, location='json')
        parser.add_argument('sections', type=list, location='json')
        parser.add_argument('sidebar_content', type=str)
        parser.add_argument('is_published', type=bool)
        parser.add_argument('is_featured', type=bool)
        parser.add_argument('author', type=str)
        parser.add_argument('publish_date', type=str)
        parser.add_argument('parent_page_id', type=int)
        parser.add_argument('order_position', type=int)
        parser.add_argument('template_name', type=str)

        args = parser.parse_args()
        
        # Convert publish_date string to date object if provided
        if args.get('publish_date'):
            args['publish_date'] = datetime.strptime(args['publish_date'], '%Y-%m-%d').date()
        
        updated = Page.update(id, **args)
        if not updated:
            return {"message": "Page not found."}, 404

        return jsonify(updated.to_dict())

    def delete(self, id):
        deleted = Page.delete_by_id(id)
        if not deleted:
            return {"message": "Page not found."}, 404

        return {"message": f"Page with id {id} deleted successfully."}, 200

class PageBySlugDetail(Resource):
    def get(self, slug):
        page = Page.query.filter_by(slug=slug).first()
        if not page:
            return {"message": "Page not found."}, 404
        
        # Increment view count
        page.view_count += 1
        page.save()
        
        return jsonify(page.to_dict())
