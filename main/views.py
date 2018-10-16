from main.model import ProductList,api

api.add_resource(ProductList, '/api/v1/product/<string:name>')