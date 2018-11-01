from flask_restful import Resource, reqparse
from storeapi.views.parse import parser
from storeapi.models.model import User
from flask_jwt_extended import create_access_token
import datetime

class LogIn(Resource):
    def post(self):
        data = parser.parse_args()
        user_information = User.get_user_by_username(data['username']) 
        identity = dict(user_id = user_information.get('user_id'), admin_status = user_information.get('isadmin') )
        if user_information:
            if User.verify_hash(data['password'],user_information['password'] ):
                expires = datetime.timedelta(days=1)
                auth_token = create_access_token(identity=identity, expires_delta=expires)
                response = {
                            "access_token": auth_token,
                            "status": "true",
                            "message": "user logged in successfully",
                            "user":{"username": data["username"]}
                            }, 200
                return response
            return {"status": "fail", "error": "login failed"}, 401       
            

        
       
           