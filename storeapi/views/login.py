from flask_restful import Resource
from storeapi.views.parse import parser
from storeapi.models.model import User
from flask_jwt_extended import create_access_token
import datetime


class LogIn(Resource):
    def post(self):
        data = parser.parse_args()
        username = data['Username'].lower()
        user_information = User.get_user_by_username(username)
        identity = dict(user_id=user_information.get('user_id'), admin_status=user_information.get('isadmin'))
        if user_information:
            if User.verify_hash(data['Password'], user_information['password']):
                expires = datetime.timedelta(days=1)
                auth_token = create_access_token(identity=identity, expires_delta=expires)
                response = {
                            "Access_token": auth_token,
                            "Message": "Login successful",
                            "User": {"username": data["Username"]}
                            }
                return response, 200
            return {"Error": "Login failed"}, 401
