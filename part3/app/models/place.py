from .basemodel import BaseModel
from app import db
from .user import User
from .place_amenity import Place_Amenity
from sqlalchemy.orm import relationship


class Place(BaseModel):
    __tablename__ = "places"

    _title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String)
    _price = db.Column(db.Float, nullable=False)
    _latitude = db.Column(db.Float, nullable=False)
    _longitude = db.Column(db.Float, nullable=False)
    _owner_id = db.Column("owner_id", db.String(36),
                         db.ForeignKey("users.id", ondelete="CASCADE"),
                         nullable=False)
    reviews = relationship("Review", backref="place", lazy=True)
    amenities = relationship("Amenity",
                             secondary=Place_Amenity,
                             backref="Place_Amenity", lazy=True)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty")
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        super().is_max_length('title', value, 100)
        self._title = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError("Price must be a float")
        if value < 0:
            raise ValueError("Price must be positive.")
        self._price = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, float):
            raise TypeError("Latitude must be a float")
        super().is_between("latitude", value, -90, 90)
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, float):
            raise TypeError("Longitude must be a float")
        super().is_between("longitude", value, -180, 180)
        self._longitude = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise TypeError("Owner must be a user instance")
        self._owner = value

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def delete_review(self, review):
        """Add an amenity to the place."""
        self.reviews.remove(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner_id': self.owner.id
        }

    def to_dict_list(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'owner': self.owner.to_dict(),
            'amenities': self.amenities,
            'reviews': self.reviews
        }