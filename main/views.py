from main.model import Product,api

api.add_resource(Product, '/api/v1/product/<string:name>')