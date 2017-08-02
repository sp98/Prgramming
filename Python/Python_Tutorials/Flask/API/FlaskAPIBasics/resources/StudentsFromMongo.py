from flask import jsonify, Blueprint, make_response

from flask_restful import (Resource, Api, reqparse, inputs, request,
                           fields, marshal, marshal_with, abort)


import StudentStore


student_response = {
    'id' : fields.String,
    'name' : fields.String,
    'age' : fields.Integer,
    'profession': fields.String
}


class StudentList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        # adding arguments for each field:
        self.reqparse.add_argument('id',
                                   required=True,
                                   nullable=True,
                                   location=['form', 'json'],
                                   help="Please provide an ID",
                                   type=int)
        self.reqparse.add_argument('name',
                                   required=True,
                                   help='No name provided!',
                                   location=['form', 'json'])
        self.reqparse.add_argument('age',
                                    required=True,    # wether this field is required or not
                                    help = 'No age provided!',  # message displayed when field is missing
                                    location=['form', 'json'],  # where to check these requests from
                                    type=inputs.positive)    # validate the type
        self.reqparse.add_argument('profession',
                                   required=False,
                                   nullable=True,
                                   location=['form', 'json'],
                                   default='Not a Pro!')

        super().__init__()

    def get(self):
        return StudentStore.get_student_info()

    def post(self):
        args = self.reqparse.parse_args()
        StudentStore.store_student_info(args)


class Student(Resource):
    def get(self, student_id):
        return StudentStore.get_student_info(student_id)

    def delete(self, student_id):
        StudentStore.delete_student_info(student_id)


students_api = Blueprint('resources.Students', __name__)
api = Api(students_api)
api.add_resource(
      StudentList,
      '/api/v2/students',
      endpoint='students'
)

api.add_resource(
      Student,
      '/api/v2/student/<int:student_id>',
      endpoint='student'
)