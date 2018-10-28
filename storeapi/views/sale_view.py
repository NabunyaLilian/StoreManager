"""
   A file for defining sale resource
"""
from flask_restful import Resource
from storeapi.models.model import sales
from storeapi.views.check import check_id

class Sale(Resource):
    """
       class for sale resource
   """
    def get(self, sale_id):
        """
           method to get a specific sale
        """
        sale = check_id(sale_id , sales ,'sale_id') 
        if sale:
           return sale
        return {'message':'resource not found'}
      
    