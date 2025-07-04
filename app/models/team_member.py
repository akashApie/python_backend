from .base import db, BaseModel
from sqlalchemy.dialects.mysql import JSON

class TeamMember(BaseModel):
    __tablename__ = "team_members"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(50), nullable=False)  # research, conservation, education, administration
    specialization = db.Column(db.String(200), nullable=True)
    bio = db.Column(db.Text, nullable=False)
    education = db.Column(JSON, nullable=True)  # List of educational qualifications
    experience_years = db.Column(db.Integer, nullable=True)
    research_interests = db.Column(JSON, nullable=True)  # List of research interests
    publications = db.Column(JSON, nullable=True)  # List of publications
    awards = db.Column(JSON, nullable=True)  # List of awards and recognitions
    profile_image = db.Column(db.String(255), nullable=False)
    gallery_images = db.Column(JSON, nullable=True)
    email = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    linkedin_url = db.Column(db.String(255), nullable=True)
    orcid_id = db.Column(db.String(50), nullable=True)
    languages_spoken = db.Column(JSON, nullable=True)
    current_projects = db.Column(JSON, nullable=True)  # List of current project names
    join_date = db.Column(db.Date, nullable=True)
    is_public = db.Column(db.Boolean, default=True)
    is_featured = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position,
            'department': self.department,
            'specialization': self.specialization,
            'bio': self.bio,
            'education': self.education,
            'experience_years': self.experience_years,
            'research_interests': self.research_interests,
            'publications': self.publications,
            'awards': self.awards,
            'profile_image': self.profile_image,
            'gallery_images': self.gallery_images,
            'email': self.email,
            'phone': self.phone,
            'linkedin_url': self.linkedin_url,
            'orcid_id': self.orcid_id,
            'languages_spoken': self.languages_spoken,
            'current_projects': self.current_projects,
            'join_date': self.join_date.isoformat() if self.join_date else None,
            'is_public': self.is_public,
            'is_featured': self.is_featured,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    @classmethod
    def create(cls, **kwargs):
        member = cls(**kwargs)
        return member.save()

    @classmethod
    def update(cls, id, **kwargs):
        member = cls.query.get(id)
        if not member:
            return None
        
        for key, value in kwargs.items():
            if hasattr(member, key) and value is not None:
                setattr(member, key, value)

        return member.save()

    @classmethod
    def delete_by_id(cls, id):
        member = cls.query.get(id)
        if not member:
            return None
        
        member.delete()
        return True
