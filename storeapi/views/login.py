from flask_restful import Resource, reqparse
from storeapi.views.parse import parser
from storeapi.models.model import User
from flask_jwt_extended import create_access_token
import datetime

class LogIn(Resource):
    def post(self):
        data = parser.parse_args()
        return data
        user_information = User.get_user_by_username(data["username"])
        print (user_informations)
        if user_information:
           if User.verify_hash(data["password"],user_information["password"]):
                expires_at = datetime.timedelta(days=1)
                jwt_token = create_access_token(identity=user_information['id'], expires_delta=expires_at)
                return {"status": "success", "message": "successfully logged in",
                        "jwt_token": auth_token,"users_name": user_information["name"]}, 200

        return {"status": "fail", "message": "Unauthorised Access. username or password"}, 401   