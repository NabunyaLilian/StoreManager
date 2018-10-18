from flask import request
from flask_restful import Resource
from storeapi.models.model import products

class ProductList(Resource):
    def get(self):
        return {'products': products}
    
    def post(self): 
        if request.content_type == 'application/json':
           data = request.get_json()
           name = data.get('name')
           quantity = data.get('quantity')
           price = data.get('price')
           min_quantity = data.get('min_quantity')
           category = data.get('category')
           string_data = [name,category] 
           int_data = [quantity,price,min_quantity]
        if all(isinstance(x, str) for x in string_data) and all(isinstance(x, int) for x in int_data):
            product = { 'product_id':len(products) +1,'name':name,'quantity':quantity,'price':price,'min_quantity':min_quantity,'category':category}
            products.append(product)
            return product ,201
        else:
            return {"message":"Enter valid values please"}   
 