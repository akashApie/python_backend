from .base import db, BaseModel
from sqlalchemy.dialects.mysql import JSON

class AboutUs(BaseModel):
    __tablename__ = "aboutus"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=false, index=True)
    text = db.Column(db.Text, unique=True, nullable=false, index=True)
    image = db.Column(db.String, unique=True, nullable=false, index=True)
    additional_images = db.Column(JSON, nullable=True)
    information = db.Column(db.Text, unique=True, nullable=false, index=True)
    additional_information = db.Column(db.Text, unique=True, nullable=false, index=True)

    @classmethod
    def create(cls, title, text, image, information, additional_information,additional_images):
        about = cls(
            title=title,
            text=text,
            image=image,
            information=information,
            additional_images=additional_images,
            additional_information=additional_information
        )

        return about.save()

    @classmethod
    def update(cls, id, **kwargs):
        about = cls.query.get(id)
        if not about:
            return None
        
        for key,value in kwargs.items():
            if hasattr(about, key):
                setattr(about, key, value)

        return about.save()

    @classmethod
    def delete_by_id(cls,id):
        about = cls.query.get(id)
        if not about:
            return None
        
        return about.delete()
