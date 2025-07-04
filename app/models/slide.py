from .base import db, BaseModel
from sqlalchemy.dialects.mysql import JSON

class Slide(BaseModel):
    __tablename__ = "slides"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subtitle = db.Column(db.String(300), nullable=True)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(255), nullable=False)
    background_image = db.Column(db.String(255), nullable=True)
    call_to_action_text = db.Column(db.String(100), nullable=True)
    call_to_action_url = db.Column(db.String(255), nullable=True)
    order_position = db.Column(db.Integer, nullable=False, default=0)
    category = db.Column(db.String(50), nullable=False)  # hero, featured, announcement
    is_active = db.Column(db.Boolean, default=True)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    overlay_color = db.Column(db.String(20), nullable=True)  # hex color for overlay
    text_color = db.Column(db.String(20), default='#ffffff')
    animation_type = db.Column(db.String(30), default='fade')  # fade, slide, zoom
    display_duration = db.Column(db.Integer, default=5000)  # in milliseconds

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'subtitle': self.subtitle,
            'description': self.description,
            'image_url': self.image_url,
            'background_image': self.background_image,
            'call_to_action_text': self.call_to_action_text,
            'call_to_action_url': self.call_to_action_url,
            'order_position': self.order_position,
            'category': self.category,
            'is_active': self.is_active,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'overlay_color': self.overlay_color,
            'text_color': self.text_color,
            'animation_type': self.animation_type,
            'display_duration': self.display_duration,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    @classmethod
    def create(cls, **kwargs):
        slide = cls(**kwargs)
        return slide.save()

    @classmethod
    def update(cls, id, **kwargs):
        slide = cls.query.get(id)
        if not slide:
            return None
        
        for key, value in kwargs.items():
            if hasattr(slide, key) and value is not None:
                setattr(slide, key, value)

        return slide.save()

    @classmethod
    def delete_by_id(cls, id):
        slide = cls.query.get(id)
        if not slide:
            return None
        
        slide.delete()
        return True
