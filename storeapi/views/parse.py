from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('username', help ='This field cannot be left blank', required = True)
parser.add_argument('password', help ='This field cannot be left blank', required = True)
