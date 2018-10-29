"""
   A file initializing flask and defining routes hhjkjkjk
"""
from flask import Flask
from flask_restful import Api
from storeapi.views.product_view import Product
from storeapi.views.products_list_view import ProductList
from storeapi.views.sale_view import Sale
from storeapi.views.sales_view import Sales
from instance import config
from instance.config import app_config
  
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile(config.py)
    api = Api(app)

    api.add_resource(Product, '/api/v1/product/<int:product_id>')
    api.add_resource(ProductList, '/api/v1/products')

    api.add_resource(Sale, '/api/v1/sale/<int:sale_id>')
    api.add_resource(Sales, '/api/v1/sales')