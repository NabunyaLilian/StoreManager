"""
   A file for defining product_view resource
"""
from flask_restful import Resource

from storeapi.models.products import Products
from flask_jwt_extended import jwt_required, get_jwt_identity


class Product(Resource):
    """
       class for product resource
    """
    def get(self, product_id):
        """
           method to get a specific product
        """
 
        product = Products.get_product_by_id(product_id)
        if product:
           return {
                    'product' : product
                 }, 200
        return {"message":"product doesnot exist"},404 
    @jwt_required    
    def put (self,product_id):
        """
           method to update products
        """
        data = Products.parse()
        product_obj = Products(data['name'],data['quantity'],data['price'],data['min_quantity'],data['category']) 
        user_identity = get_jwt_identity()
        if not user_identity['admin_status'] :
           return {"Error":"Access denied"}
        if product_obj.check_empty_fields() == True:
            return {"Error":"Field empty field detected, make sure all fields have values"}, 400    
        if product_obj.search_special_characters() == False:
            return {"Error":"No string should contain special characters"},400                  
        if product_obj.check_field_numeric() == False :
                return {"Error":"name should not contain numbers"},400 
        if product_obj.check_empty_space():
                return {"Error":"space detected in one of the fields"},400        
        new_product = product_obj.update_products(product_id) 
        if new_product:
            response =  {
                                    "message": "product updated successfully",
                                    "user": {
                                        "name": data['name'],
                                        "quantity" : data['quantity'],
                                        "price": data['price'],
                                        "min_quantity":data['min_quantity'],
                                        "category": data['category'] }
                                }, 202
            return response                    

    def delete(self,product_id):
        """
           method to delete a specific product
        """
        product = Products.get_product_by_id(product_id)       
        if product:
            Products.delete_product(product_id) 
            return {"message": "product is successfully deleted"},200
        else:
            return {"Error":"product not found"},404    

