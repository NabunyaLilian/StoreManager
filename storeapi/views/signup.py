import psycopg2
from psycopg2.extras import RealDictCursor
from flask_restful import Resource
from flask_restful import reqparse
from storeapi.models.model import User
from flask_jwt_extended import jwt_required, get_jwt_identity
import datetime

class SignUp(Resource):
    
    @jwt_required 
    def post(self):
        data = User.parse()
        user = User(data['Username'],data['FirstName'],data['Password'],data['isAdmin'])
        user_identity = get_jwt_identity()
        if not user_identity['admin_status'] :
            return {"Error":"Access denied"}
        if user.check_empty_fields() :
            return {"Error":"Field empty field detected, make sure all fields have values"}, 400    
        if not user.validate_data_type :
            return {"Error":"name should only contain alphabetical letters"},400 
        if not user.search_special_characters() :
            return {"Error":"No string should contain special characters"},400                  
        if user.check_field_numeric() != None :
                return {"Error":"name should not contain numbers"},400 
        if user.check_empty_space() :
                return {"Error":"space detected in one of the fields"},400 
        if User.check_length_restrictions(['Name','Username','Password'],[data['Username'],data['FirstName'],data['Password']]):
                return {"Error":"length should be 255 charactres"},400
        user_information = User.get_user_by_username(data['Username']) 
        if  user_information: 
            return {"message":"username already exists"}
        else:
            user.create_user()   
            
            return {
                    "message": "account created",
                    "user":{"username": data["Username"],"firstname": data['FirstName']}
                    }, 201

        
