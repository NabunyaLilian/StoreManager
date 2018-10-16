from main.model import Sale,api

api.add_resource(Sale, '/api/v1/sale/<string:name>')
