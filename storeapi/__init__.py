"""
   A file initializing flask and defining routes hhjkjkjk
"""

from flask import Flask
from flask_jwt_extended import JWTManager 
from flask_restful import Api
from storeapi.views.product_view import Product
from storeapi.views.products_list_view import ProductList
from storeapi.views.sale_view import SaleView
from storeapi.views.sales_view import Sales
from storeapi.views.login import LogIn
from storeapi.views.signup import SignUp
from flask_cors import CORS
import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'secret_storeapi_key'
jwt = JWTManager(app)
api = Api(app)


api.add_resource(Product, '/api/v2/product/<int:product_id>')
api.add_resource(ProductList, '/api/v2/products')

api.add_resource(SaleView, '/api/v2/sale/<int:sale_id>')
api.add_resource(Sales, '/api/v2/sales')
api.add_resource(SignUp, '/api/v2/auth/signup') 
api.add_resource(LogIn, '/api/v2/auth/login')



