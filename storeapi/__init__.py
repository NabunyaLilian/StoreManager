"""
   A file initializing flask and defining routes
"""

from flask import Flask
from flask_jwt_extended import JWTManager 
from flask_restful import Api
from storeapi.views.product_view import Product
from storeapi.views.products_list_view import ProductList
from storeapi.views.sale_view import Sale
from storeapi.views.sales_view import Sales
from storeapi.views.login import LogIn
from storeapi.views.signup import SignUp
from storeapi.views.logout import LogOut
import sys
import os.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret_storeapi_key'
jwt = JWTManager(app)
api = Api(app)

api.add_resource(Product, '/api/v2/product/<int:product_id>')
api.add_resource(ProductList, '/api/v2/products')

api.add_resource(Sale, '/api/v2/sale/<int:sale_id>')
api.add_resource(Sales, '/api/v2/sales')
api.add_resource(SignUp, '/api/v2/auth/signup') 
api.add_resource(LogIn, '/api/v2/auth/login')
api.add_resource(LogOut,'/api/v2/logout')

