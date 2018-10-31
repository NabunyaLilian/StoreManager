"""
   A file for defining sale resource
"""
from flask_restful import Resource
from storeapi.models.sale import Sale

class Sale(Resource):
    """
       class for sale resource
   """
    def get(self, sale_id):
        """
           method to get a specific sale
        """
        pass