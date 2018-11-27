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
                    'Product': [product]
                 }, 200
        return {"Message": "Product not in stock"}, 404

    @jwt_required
    def put(self, product_id):
        """
           method to update products
        """
        data = Products.parse()
        data = Products.parse()
        name =  data['Name'].lower()   
        quantity = data['Quantity'].lower()
        price = data['Price'].lower()
        min_quantity = data['Min_quantity'].lower()
        category = data['Category'].lower()
        product_obj = Products(name, quantity, price, min_quantity, category)
        user_identity = get_jwt_identity()
        if user_identity['admin_status'] != 'True':
            return {"Error": "Access denied"}, 401
        if product_obj.check_empty_fields():
            return {"Error": "Field empty field detected, make sure all fields have values"}, 400
        if product_obj.search_special_characters():
            return {"Error": "No string should contain special characters"}, 400
        if product_obj.check_field_numeric() is not None:
                return {"Error": "Name should not contain numbers"}, 400
        if product_obj.check_empty_space():
                return {"Error": "Space detected in one of the fields"}, 400
        product = Products.get_product_by_id(product_id)
        if product:        
            new_product = product_obj.update_products(product_id)
            if new_product:
                response = {
                                        "Message": "Product updated",
                                        "Product": {
                                            "Name": data['Name'],
                                            "Quantity": data['Quantity'],
                                            "Price": data['Price'],
                                            "Min_Quantity": data['Min_quantity'],
                                            "Category": data['Category']}
                                    }, 202
                return response
            else:
                return {'Error', 'Something went wrong'}, 406
        return {"Message": "Product not in stock"}, 404

    def delete(self, product_id):
        """
           method to delete a specific product
        """
        product = Products.get_product_by_id(product_id)
        if product:
            Products.delete_product(product_id)
            return {"Message": "Product deleted"}, 200
        else:
            return {"Error": "Product not found"}, 404
