from .basemodel import BaseModel
from app.extensions import db
from sqlalchemy.orm import relationship
import uuid


amenity_place = db.Table("amenity_place",
                          db.Column("amenity_id",
                                    db.String,
                                    db.ForeignKey("amenities.id", ondelete="CASCADE"),
                                    nullable=False, primary_key=True),
                          db.Column("place_id",
                                    db.String,
                                    db.ForeignKey("places.id", ondelete="CASCADE"),
                                    nullable=False, primary_key=True)
                          )

class Amenity(BaseModel):
    __tablename__ = "amenities"

    id = db.Column(db.String(36), primary_key=True,
                   default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(50), nullable=False)
    places = relationship("Place", secondary=amenity_place, backref="place_amenities", lazy=True)

    """@property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not value:
            raise ValueError("Name cannot be empty")
        super().is_max_length('Name', value, 50)
        self.__name = value"""

    def update(self, data):
        return super().update(data)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
