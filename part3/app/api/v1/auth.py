from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models.user import User
from app.services import facade
from flask import request
import json

api = Namespace('auth', description='Authentication operations')

# Model for input validation
login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@api.route('/login')
@api.response(401, 'User not found')
@api.response(200, 'User authenticated successfully')
@api.response(400, 'Invalid credential')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Authenticate user and return a JWT token"""
        user_data = request.json
        email = user_data.get('email')
        password = user_data.get('password')
        
        # Step 1: Retrieve the user based on the provided email
        user = facade.get_user_by_email(email)
        if not user or not email or not user.verify_password(password):
            return {'error': 'Invalid credential'}, 400
        
        # Step 2: Check if the user exists and the password is correct
        if not email or not password:
            return {'error': 'Invalid credential'}, 400
        # Step 3: Create a JWT token with the user's id and is_admin flag
        access_token = create_access_token(identity=({'id': str(user.id), 'is_admin': user.is_admin}))
        
        # Step 4: Return the JWT token to the client
        return {'access_token': access_token}, 200

@api.route('/protected')
class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        """A protected endpoint that requires a valid JWT token"""
        current_user = json.loads(get_jwt_identity())  # Retrieve the user's identity from the token
        return {'message': f'Hello, user {current_user["id"]}'}, 200
