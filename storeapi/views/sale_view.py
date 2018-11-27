"""
   A file for defining sale resource
"""
from flask_restful import Resource
from storeapi.models.sale import Sale
from flask_jwt_extended import jwt_required, get_jwt_identity


class SaleView(Resource):
    """
       class for sale resource
   """
    @jwt_required
    def get(self, user_id):
        """
           method to get a specific sale
        """
        identity = get_jwt_identity()
        if identity['admin_status'] == 'True':
            sale = Sale.get_sale_by_userid(user_id)
            if sale:
                return {'Sale': sale}, 200
            else:
                return {'Error': 'Sale record doesnot exist'}, 404
        elif identity['user_id'] == user_id:
            sale = Sale.get_sale_by_userid(user_id)
            if sale:
                return {'Sale': sale}, 200
            else:
                return {'Error': 'Sale record doesnot exist'}, 404
        else:
            return{'Error':'Something went wrong'}