from .base import db, BaseModel
from sqlalchemy.dialects.mysql import JSON

class ConservationProject(BaseModel):
    __tablename__ = "conservation_projects"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subtitle = db.Column(db.String(300), nullable=True)
    category = db.Column(db.String(50), nullable=False)  # research, breeding, field_work, education
    status = db.Column(db.String(30), nullable=False)  # ongoing, completed, upcoming
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    objectives = db.Column(JSON, nullable=False)  # List of objectives
    methodology = db.Column(db.Text, nullable=True)
    results = db.Column(db.Text, nullable=True)
    impact = db.Column(db.Text, nullable=True)
    main_image = db.Column(db.String(255), nullable=False)
    gallery_images = db.Column(JSON, nullable=True)
    species_involved = db.Column(JSON, nullable=True)  # List of species names
    partners = db.Column(JSON, nullable=True)  # List of partner organizations
    funding_sources = db.Column(JSON, nullable=True)
    budget = db.Column(db.String(50), nullable=True)
    lead_researcher = db.Column(db.String(100), nullable=True)
    publications = db.Column(JSON, nullable=True)  # List of related publications
    is_featured = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'subtitle': self.subtitle,
            'category': self.category,
            'status': self.status,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'location': self.location,
            'description': self.description,
            'objectives': self.objectives,
            'methodology': self.methodology,
            'results': self.results,
            'impact': self.impact,
            'main_image': self.main_image,
            'gallery_images': self.gallery_images,
            'species_involved': self.species_involved,
            'partners': self.partners,
            'funding_sources': self.funding_sources,
            'budget': self.budget,
            'lead_researcher': self.lead_researcher,
            'publications': self.publications,
            'is_featured': self.is_featured,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    @classmethod
    def create(cls, **kwargs):
        project = cls(**kwargs)
        return project.save()

    @classmethod
    def update(cls, id, **kwargs):
        project = cls.query.get(id)
        if not project:
            return None
        
        for key, value in kwargs.items():
            if hasattr(project, key) and value is not None:
                setattr(project, key, value)

        return project.save()

    @classmethod
    def delete_by_id(cls, id):
        project = cls.query.get(id)
        if not project:
            return None
        
        project.delete()
        return True
