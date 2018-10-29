from flask_restful import Resource
from storeapi.views.parse import parser
from storeapi.models.model import User
from flask_jwt_extended import create_access_token
import datetime

class SignUp(Resource):
    def post(self):
        data = parser.parse_args()
        user_information = User.get_user_by_username(data["username"])
        if not user_information:
            password = User.generate_hash(data["username"],user_information['password'])
