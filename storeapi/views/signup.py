import psycopg2
from psycopg2.extras import RealDictCursor
from flask_restful import Resource
from flask_restful import reqparse
from storeapi.models.model import User
from flask_jwt_extended import create_access_token
import datetime

class SignUp(Resource):
    def post(self):
        data = User.parse()
        user = User(data['username'],data['name'],data['password'],data['isAdmin'])
        if not user.check_empty_fields():
            return {"Error":"Field empty field detected, make sure all fields have values"}, 400
        if user.validate_data_type():  
            return {"Error": "Make sure every field has the right datatype"},400   
        if user.search_special_characters():
            return {"Error":"No string should contain special characters"},400                  
        if user.check_field_numeric() :
                return {"Error":"name should not contain numbers"},400 

        user_information = user.get_user_by_username() 
        if  user_information: 
            return {"message":"username already exists"}
        else:
            create_user = user.create_user()   
            if create_user:
                response =  {
                                "message": "user registered successfully",
                                "user": {
                                    "username": data['username'],
                                    "name": data['name'] }
                            }, 201
                return response           
        
        