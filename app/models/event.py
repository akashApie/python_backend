from .base import db, BaseModel
from sqlalchemy.dialects.mysql import JSON

class Event(BaseModel):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subtitle = db.Column(db.String(300), nullable=True)
    category = db.Column(db.String(50), nullable=False)  # workshop, guided_tour, special_event, educational_program
    event_type = db.Column(db.String(30), nullable=False)  # public, private, school_group, research
    start_datetime = db.Column(db.DateTime, nullable=False)
    end_datetime = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    venue_details = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=False)
    detailed_agenda = db.Column(db.Text, nullable=True)
    target_audience = db.Column(db.String(100), nullable=False)
    max_participants = db.Column(db.Integer, nullable=True)
    current_registrations = db.Column(db.Integer, default=0)
    registration_fee = db.Column(db.Float, default=0.0)
    prerequisites = db.Column(db.Text, nullable=True)
    what_to_bring = db.Column(JSON, nullable=True)  # List of items
    main_image = db.Column(db.String(255), nullable=False)
    gallery_images = db.Column(JSON, nullable=True)
    organizers = db.Column(JSON, nullable=True)  # List of organizer names
    guest_speakers = db.Column(JSON, nullable=True)
    registration_link = db.Column(db.String(255), nullable=True)
    contact_person = db.Column(db.String(100), nullable=True)
    contact_email = db.Column(db.String(100), nullable=True)
    contact_phone = db.Column(db.String(20), nullable=True)
    is_featured = db.Column(db.Boolean, default=False)
    is_cancelled = db.Column(db.Boolean, default=False)
    cancellation_reason = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'subtitle': self.subtitle,
            'category': self.category,
            'event_type': self.event_type,
            'start_datetime': self.start_datetime.isoformat() if self.start_datetime else None,
            'end_datetime': self.end_datetime.isoformat() if self.end_datetime else None,
            'location': self.location,
            'venue_details': self.venue_details,
            'description': self.description,
            'detailed_agenda': self.detailed_agenda,
            'target_audience': self.target_audience,
            'max_participants': self.max_participants,
            'current_registrations': self.current_registrations,
            'registration_fee': self.registration_fee,
            'prerequisites': self.prerequisites,
            'what_to_bring': self.what_to_bring,
            'main_image': self.main_image,
            'gallery_images': self.gallery_images,
            'organizers': self.organizers,
            'guest_speakers': self.guest_speakers,
            'registration_link': self.registration_link,
            'contact_person': self.contact_person,
            'contact_email': self.contact_email,
            'contact_phone': self.contact_phone,
            'is_featured': self.is_featured,
            'is_cancelled': self.is_cancelled,
            'cancellation_reason': self.cancellation_reason,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    @classmethod
    def create(cls, **kwargs):
        event = cls(**kwargs)
        return event.save()

    @classmethod
    def update(cls, id, **kwargs):
        event = cls.query.get(id)
        if not event:
            return None
        
        for key, value in kwargs.items():
            if hasattr(event, key) and value is not None:
                setattr(event, key, value)

        return event.save()

    @classmethod
    def delete_by_id(cls, id):
        event = cls.query.get(id)
        if not event:
            return None
        
        event.delete()
        return True
