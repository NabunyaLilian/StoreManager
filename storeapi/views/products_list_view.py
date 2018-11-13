"""
   A file for defining products list view resource
"""
from flask_restful import Resource
from storeapi.models.products import Products
from flask_jwt_extended import jwt_required, get_jwt_identity


class ProductList(Resource):
    """
       class for product list
    """
    def get(self):
        """
        method to get all products

        """
        products = Products.get_all_products()
        return {'Products': products}, 200

    @jwt_required
    def post(self):
        """
        method to create a product
        """
        data = Products.parse()
        name =  data['Name'].lower()   
        quantity = data['Quantity'].lower()
        price = data['Price'].lower()
        min_quantity = data['Min_quantity'].lower()
        category = data['Category'].lower()
        product_obj = Products(name, quantity, price, min_quantity, category)
        user_identity = get_jwt_identity()
        if user_identity['admin_status'] == 'False':
            return {"Error": "Access denied"}, 401
        if product_obj.check_empty_fields():
            return {"Error": "Field empty field detected, make sure all fields have values"}, 400
        if product_obj.search_special_characters():
            return {"Error": "No string should contain special characters"}, 400
        if product_obj.check_field_numeric() is not None:
                return {"Error": "name should not contain numbers"}, 400
        if product_obj.check_empty_space():
                return {"Error": "space detected in one of the fields"}, 400    
        product_dict = Products.get_product_by_name(name)
        if  not product_dict:
            product_obj.create_product()
            response = {
                                "Message": "Product added to stock",
                                "Product": {
                                    "Name": data['Name'],
                                    "Price": data['Price']}
                            }, 201
            return response
        else:
            return {'Error': 'Product already in stock'}, 400
