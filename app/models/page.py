from .base import db, BaseModel
from sqlalchemy.dialects.mysql import JSON

class Page(BaseModel):
    __tablename__ = "pages"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False, index=True)
    page_type = db.Column(db.String(50), nullable=False)  # static, dynamic, landing
    content = db.Column(db.Text, nullable=False)
    meta_description = db.Column(db.String(300), nullable=True)
    meta_keywords = db.Column(JSON, nullable=True)  # List of keywords
    main_image = db.Column(db.String(255), nullable=True)
    gallery_images = db.Column(JSON, nullable=True)
    sections = db.Column(JSON, nullable=True)  # List of page sections with content
    sidebar_content = db.Column(db.Text, nullable=True)
    is_published = db.Column(db.Boolean, default=True)
    is_featured = db.Column(db.Boolean, default=False)
    view_count = db.Column(db.Integer, default=0)
    author = db.Column(db.String(100), nullable=True)
    publish_date = db.Column(db.Date, nullable=True)
    parent_page_id = db.Column(db.Integer, db.ForeignKey('pages.id'), nullable=True)
    order_position = db.Column(db.Integer, default=0)
    template_name = db.Column(db.String(50), default='default')

    # Self-referential relationship for parent-child pages
    children = db.relationship('Page', backref=db.backref('parent', remote_side=[id]))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'page_type': self.page_type,
            'content': self.content,
            'meta_description': self.meta_description,
            'meta_keywords': self.meta_keywords,
            'main_image': self.main_image,
            'gallery_images': self.gallery_images,
            'sections': self.sections,
            'sidebar_content': self.sidebar_content,
            'is_published': self.is_published,
            'is_featured': self.is_featured,
            'view_count': self.view_count,
            'author': self.author,
            'publish_date': self.publish_date.isoformat() if self.publish_date else None,
            'parent_page_id': self.parent_page_id,
            'order_position': self.order_position,
            'template_name': self.template_name,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    @classmethod
    def create(cls, **kwargs):
        page = cls(**kwargs)
        return page.save()

    @classmethod
    def update(cls, id, **kwargs):
        page = cls.query.get(id)
        if not page:
            return None
        
        for key, value in kwargs.items():
            if hasattr(page, key) and value is not None:
                setattr(page, key, value)

        return page.save()

    @classmethod
    def delete_by_id(cls, id):
        page = cls.query.get(id)
        if not page:
            return None
        
        page.delete()
        return True
