"""
   A file for defining products list view resource
"""
from flask_restful import Resource
from storeapi.models.model import User
from flask_jwt_extended import jwt_required, get_jwt_identity


class AdminRights(Resource):
    """
       class for product list
    """
    @jwt_required
    def put(self,user_id):
        identity = get_jwt_identity()
        if identity['admin_status'] == 'True':
            User.admin_rights(user_id)
            return {
                    "Message": "New admin created"
                   }, 202
        return {"Error": "You have no prior access to this resource"}            