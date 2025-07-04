from .base import db, BaseModel
from sqlalchemy.dialects.mysql import JSON

class Species(BaseModel):
    __tablename__ = "species"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, index=True)
    scientific_name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # reptile, amphibian
    conservation_status = db.Column(db.String(50), nullable=False)
    habitat = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    diet = db.Column(db.Text, nullable=False)
    size = db.Column(db.String(100), nullable=False)
    lifespan = db.Column(db.String(50), nullable=False)
    main_image = db.Column(db.String(255), nullable=False)
    gallery_images = db.Column(JSON, nullable=True)
    interesting_facts = db.Column(JSON, nullable=True)
    breeding_info = db.Column(db.Text, nullable=True)
    threats = db.Column(db.Text, nullable=True)
    distribution = db.Column(db.Text, nullable=False)
    is_venomous = db.Column(db.Boolean, default=False)
    is_featured = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'scientific_name': self.scientific_name,
            'category': self.category,
            'conservation_status': self.conservation_status,
            'habitat': self.habitat,
            'description': self.description,
            'diet': self.diet,
            'size': self.size,
            'lifespan': self.lifespan,
            'main_image': self.main_image,
            'gallery_images': self.gallery_images,
            'interesting_facts': self.interesting_facts,
            'breeding_info': self.breeding_info,
            'threats': self.threats,
            'distribution': self.distribution,
            'is_venomous': self.is_venomous,
            'is_featured': self.is_featured,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    @classmethod
    def create(cls, **kwargs):
        species = cls(**kwargs)
        return species.save()

    @classmethod
    def update(cls, id, **kwargs):
        species = cls.query.get(id)
        if not species:
            return None
        
        for key, value in kwargs.items():
            if hasattr(species, key) and value is not None:
                setattr(species, key, value)

        return species.save()

    @classmethod
    def delete_by_id(cls, id):
        species = cls.query.get(id)
        if not species:
            return None
        
        species.delete()
        return True
