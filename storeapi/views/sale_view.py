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
    def get(self, sale_id):
        """
           method to get a specific sale
        """
        identity = get_jwt_identity()
        if identity['admin_status'] == 'True':
            sale = Sale.get_sale_by_id(sale_id)
            if sale:
                return {'Sale': sale}, 200
            else:
                return {'Error': 'Sale record doesnot exist'}, 404
