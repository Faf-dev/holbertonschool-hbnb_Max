from .basemodel import BaseModel
from app.extensions import db, bcrypt
import uuid
import re

class User(BaseModel):
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    #  self.places = []
    #  self.reviews = []

    def hash_password(self, password):
        """
        Valide et hache le mot de passe avant de le stocker.
        """
        from app import bcrypt
        if not password:
            raise ValueError("Password cannot be empty.")
        
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")

        if not re.search(r"[A-Z]", password):
            raise ValueError("Password must contain at least one uppercase letter.")
        
        if not re.search(r"[a-z]", password):
            raise ValueError("Password must contain at least one lowercase letter.")
        
        if not re.search(r"\d", password):
            raise ValueError("Password must contain at least one number.")
        
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValueError("Password must contain at least one special character.")

        # Hachage avec bcrypt
        self.__password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """
        Vérifie si le mot de passe fourni correspond au hachage stocké.
        """
        from app import bcrypt
        if not self.__password:
            return False  # Aucun mot de passe défini
        return bcrypt.check_password_hash(self.__password, password)

    # --- Méthodes annexes ---
    def add_place(self, place):
        self.places.append(place)

    def add_review(self, review):
        self.reviews.append(review)

    def delete_review(self, review):
        self.reviews.remove(review)

    @property
    def is_admin(self):
        return self.__is_admin
    
    @is_admin.setter
    def is_admin(self, value):
        if not isinstance(value, bool):
            raise TypeError("Is Admin must be a boolean")
        self.__is_admin = value

    def add_place(self, place):
        """Add a place to the user."""
        self.places.append(place)

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def delete_review(self, review):
        """Delete a review."""
        self.reviews.remove(review)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }
