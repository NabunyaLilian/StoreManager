from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('Username', help='This field cannot be left blank', required=True)
parser.add_argument('Password', help='This field cannot be left blank', required=True)
