from .basemodel import BaseModel
from .user import User
from .place import Place
from app import db


class Review(BaseModel):
    __tablename__ = 'reviews'

    _text = db.Column("text", db.String(512), nullable=False)
    _rating = db.Column("rating", db.Integer, nullable=False)
    _user_id = db.Column(db.String(36),
                        db.ForeignKey("users.id", ondelete="CASCADE"),
                        nullable=False)
    _place_id = db.Column(db.String(36),
                         db.ForeignKey("places.id", ondelete="CASCADE"),
                         nullable=False)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if not value:
            raise ValueError("Text cannot be empty")
        if not isinstance(value, str):
            raise TypeError("Text must be a string")
        self._text = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int):
            raise TypeError("Rating must be an integer")
        super().is_between('Rating', value, 1, 6)
        self._rating = value

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, value):
        if not isinstance(value, Place):
            raise TypeError("Place must be a place instance")
        self._place = value

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        if not isinstance(value, User):
            raise TypeError("User must be a user instance")
        self.__user = value

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'rating': self.rating,
            'place_id': self.place.id,
            'user_id': self.user.id
            }