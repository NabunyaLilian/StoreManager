"""
   A file for defining products list view resource
"""
from flask_restful import reqparse
from flask_restful import Resource
from storeapi.models.products import Products

class ProductList(Resource):
    """
       class for product list
    """
    def get(self):
        """
        method to get all products
        """
        data = Products.parse()
        product_obj = Products(data['name'],data['quantity'],data['price'],data['min_quantity'],data['category'])
        products = product_obj.get_all_products()
        return products 

    def post(self):
        """
        method to create a product
        """
        data = Products.parse()
        product_obj = Products(data['name'],data['quantity'],data['price'],data['min_quantity'],data['category'])
        if not product_obj.check_empty_fields():
            return {"Error":"Field empty field detected, make sure all fields have values"}, 400
        # if product_obj.validate_data_type():  
        #     return {"Error": "Make sure every field has the right datatype"},400  
        # if  product_obj.search_special_characters():
        #     return {"Error":"No string should contain special characters"},400                  
        # if  product_obj.check_field_numeric() :
        #         return {"Error":"name should not contain numbers"},401 


        product = product_obj.create_product()
        if product :
            response =  {
                                "message": "user product created successfully",
                                "user": {
                                    "name": data['name'],
                                    "price": data['price'] }
                            }, 201
            return response
        else:
            return {'message':'something went wrong'} 