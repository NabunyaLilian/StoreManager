"""
   A file for defining products list view resource
"""
from flask_restful import reqparse
from flask_restful import Resource

from storeapi.models.products import Products
from flask_jwt_extended import jwt_required, get_jwt_identity
from psycopg2.extras import RealDictCursor


class ProductList(Resource):
    """
       class for product list
    """
    def get(self):
        """
        method to get all products

        """      
        products = Products.get_all_products()
        return {'products': products }, 200
    
    @jwt_required
    def post(self):
        """
        method to create a product
        """
        data = Products.parse()
        product_obj = Products(data['name'],data['quantity'],data['price'],data['min_quantity'],data['category'])
        user_identity = get_jwt_identity()
        if  user_identity['admin_status'] != 'True' :
           return {"Error":"Access denied"}, 401
        if product_obj.check_empty_fields() :
            return {"Error":"Field empty field detected, make sure all fields have values"}, 400    
        if product_obj.search_special_characters() :
            return {"Error":"No string should contain special characters"}, 400                  
        if product_obj.check_field_numeric() != None :
                return {"Error":"name should not contain numbers"}, 400 
        if product_obj.check_empty_space() :
                return {"Error":"space detected in one of the fields"}, 400   

        product = product_obj.create_product()
        if product:
            response =  {
                                "message": "product created successfully",
                                "user": {
                                    "name": data['name'],
                                    "price": data['price'] }
                            }, 201
            return response
        else:
            return {'error':'something went wrong'}, 406


        