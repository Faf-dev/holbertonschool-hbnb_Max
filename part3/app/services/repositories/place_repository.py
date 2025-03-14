from app.models.place import Place
from app.persistence.repository import SQLAlchemyRepository


class PlaceRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Place)

    def get_places_by_user(self, user_id):
        """Retrieve all places owned by a specific user."""
        return self.model.query.filter_by(user_id=user_id).all()