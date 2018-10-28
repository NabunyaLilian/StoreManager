"""
   A file for defining products list view resource
"""
from flask import request
from flask_restful import Resource
from storeapi.models.model import products
from storeapi.views.validation import validate

class ProductList(Resource):
    """
       class for product list
    """
    def get(self):
        """
        method to get all products
        """
        return {'products': products}

    def post(self):
        """
        method to create a product
        """
        if request.content_type == 'application/json':
                data = request.get_json()
                name = data.get('name')
                quantity = data.get('quantity')
                price = data.get('price')
                min_quantity = data.get('min_quantity')
                category = data.get('category')
                string_data = [name, category]
                int_data = [quantity, price, min_quantity]
                
                if ('name' in data and 'quantity' in data and 'price' in data and 'min_quantity' in data and 'category' in data):
                    if validate(string_data,int_data):
                        if (name != "" and quantity != "" and price != "" and min_quantity != "" and category != ""):
                            product = {'product_id': len(products) +1 , 'name': name, 'quantity':quantity, 'price':price, 'min_quantity':min_quantity, 'category': category}
                            products.append(product)
                            return product, 201
                        return {"Error":"Field empty, make sure all the fields have values"}, 400    
                    return {"message":"Enter the right data type values please"}, 400
                return {'Error':'Missing field, make sure you have; name, quantity, price, min_quantity and category'}, 400    
    
    