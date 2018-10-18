from flask import request
from flask_restful import Resource
from storeapi.models.model import products

class ProductList(Resource):
    def get(self):
        return {'products': products}
    
    def post(self):
        data = request.get_json()
        product = { 'product_id':len(products) +1,'name':data['name'],'quantity':data['quantity'],'price': data['price'],'min_quantity': data['min_quantity'],'category': data['category']}
        products.append(product)
        return product ,201
 