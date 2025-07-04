from .base import db, BaseModel
from sqlalchemy.dialects.mysql import JSON

class AboutUs(BaseModel):
    __tablename__ = "aboutus"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, index=True)
    subtitle = db.Column(db.String(300), nullable=True)
    section_type = db.Column(db.String(50), nullable=False)  # mission, history, vision, team_intro, facilities
    text = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255), nullable=False, index=True)
    additional_images = db.Column(JSON, nullable=True)
    information = db.Column(db.Text, nullable=False)
    additional_information = db.Column(db.Text, nullable=False)
    subsections = db.Column(JSON, nullable=True)  # List of subsection objects
    key_points = db.Column(JSON, nullable=True)  # List of key points
    timeline_data = db.Column(JSON, nullable=True)  # For history section
    statistics = db.Column(JSON, nullable=True)  # Key statistics
    quotes = db.Column(JSON, nullable=True)  # Inspirational quotes
    order_position = db.Column(db.Integer, default=0)
    is_featured = db.Column(db.Boolean, default=False)
    is_published = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'subtitle': self.subtitle,
            'section_type': self.section_type,
            'text': self.text,
            'image': self.image,
            'additional_images': self.additional_images,
            'information': self.information,
            'additional_information': self.additional_information,
            'subsections': self.subsections,
            'key_points': self.key_points,
            'timeline_data': self.timeline_data,
            'statistics': self.statistics,
            'quotes': self.quotes,
            'order_position': self.order_position,
            'is_featured': self.is_featured,
            'is_published': self.is_published,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    @classmethod
    def create(cls, **kwargs):
        about = cls(**kwargs)
        return about.save()

    @classmethod
    def update(cls, id, **kwargs):
        about = cls.query.get(id)
        if not about:
            return None
        
        for key, value in kwargs.items():
            if hasattr(about, key) and value is not None:
                setattr(about, key, value)

        return about.save()

    @classmethod
    def delete_by_id(cls, id):
        about = cls.query.get(id)
        if not about:
            return None
        
        about.delete()
        return True
