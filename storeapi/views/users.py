"""
   A file for defining products list view resource
"""
from flask_restful import Resource
from storeapi.models.model import User
from flask_jwt_extended import jwt_required, get_jwt_identity


class Users(Resource):
    """
       class for product list
    """
    @jwt_required
    def get(self):
        """
        method to get all products

        """
        identity = get_jwt_identity()
        if identity['admin_status'] == 'True':
            users = User.get_storeattendants()
            return {'Users': users}, 200
        return {"Error": "You have no prior access to this resource"}    
