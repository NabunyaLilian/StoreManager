from flask_restful import Resource, reqparse
from storeapi.views.parse import parser
from storeapi.models.model import User
from flask_jwt_extended import create_access_token
import datetime

class LogIn(Resource):
    def post(self):
        data = parser.parse_args()
        user = User(data['username'],data['name'],data['password'],data['isAdmin'])
        user_information = user.get_user_by_username() 
        if user_information:
            response =  {
                                "message": "user logged in successfully",
                                "user": {
                                    "username": data['username'],
                                    "name": data['name'] }
                            }, 201
            return response
        

        
       
           