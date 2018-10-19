"""
   A file for defining sale resource
"""
from flask_restful import Resource
from storeapi.models.model import sales

class Sale(Resource):
    """
       class for sale resource
   """
    def get(self, sale_id):
        """
           method to get a specific sale
        """
        for sale in sales:
            if sale['sale_id'] == sale_id:
                return sale
        return {'sale': None}, 404
      