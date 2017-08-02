from flask import Flask, jsonify
from flask_restful import Resource, Api, abort
from resources.StudentsFromMongo import students_api
import resources

print(__name__)
app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/', '/hello')
app.register_blueprint(students_api)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)