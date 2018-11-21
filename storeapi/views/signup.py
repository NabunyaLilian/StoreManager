from flask_restful import Resource
from storeapi.models.model import User
from flask_jwt_extended import jwt_required, get_jwt_identity


class SignUp(Resource):

    @jwt_required
    def post(self):
        data = User.parse()
        username = data['Username'].lower()
        firstname = data['FirstName'].lower()
        password = data['Password']
        isAdmin  = data['isAdmin']
        user = User(username, firstname, password, isAdmin)
        user_identity = get_jwt_identity()
        if  user_identity['admin_status'] == 'False':
            return {"Error": "Access denied"}, 401
        if user.check_empty_fields():
            return {"Error": "Field empty field detected, make sure all fields have values"}, 400
        if user.search_special_characters():
            return {"Error": "Strings should not contain special characters"}, 400
        if user.check_field_numeric() is not None:
                return {"Error": "Name should not contain numbers"}, 400
        if user.check_empty_space():
                return {"Error": "Space detected in one of the fields"}, 400
        user_information = User.get_user_by_username(username)
        if user_information:
            return {"Message": "Username already exists"}, 400
        else:
            user.create_user()
            return {
                    "Message": "New account created",
                    "User": {"Username": data["Username"], "FirstName": data['FirstName']}
                   }, 201
