from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Simple200(Resource):
    def get(self):
        return {}

api.add_resource(Simple200, '/health')

if __name__ == '__main__':
   app.run(host="127.0.0.1", port=8080, debug=True) 