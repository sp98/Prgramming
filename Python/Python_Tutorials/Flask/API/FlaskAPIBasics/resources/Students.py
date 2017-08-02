from flask import jsonify, Blueprint, make_response

from flask_restful import (Resource, Api, reqparse, inputs, request,
                           fields, marshal, marshal_with, abort)


student_response = {
    'id' : fields.String,
    'name' : fields.String,
    'age' : fields.Integer,
    'profession': fields.String
}

students_info = [{
    'id': 1,
    'name': 'Santosh',
    'age': 26,
    'profession': 'SEDT'
    },
    {
    'id': 2,
    'name': 'Test2',
    'age': 33,
    'profession': 'Business'
    }]


class StudentList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        # adding arguments for each field:
        self.reqparse.add_argument('name',
                                   required=True,
                                   help = 'No name provided!',
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
        return jsonify(students_info)

    def post(self):
        args = self.reqparse.parse_args()
        if len(students_info) == 0:
            new_student = {
                'id': 1,
                'name': request.json['name'],
                'age': request.json['age'],
                'profession': request.json['profession']
            }
        else:
            new_student ={
                'id': students_info[-1]['id'] + 1,
                'name': request.json['name'],
                'age': request.json['age'],
                'profession': request.json['profession']
            }

        students_info.append(new_student)

        return students_info


class Student(Resource):
    def get(self, student_id):
        print(student_id)
        student = [student for x, student in enumerate(students_info) if students_info[x]['id'] == student_id]
        print(student)
        if len(student) == 0:
            abort(404)
        return jsonify({'student': student[0]})

    def delete(self, student_id):
        student = [student for x, student in enumerate(students_info) if students_info[x]['id'] == student_id]
        print(student)
        if len(student) == 0:
            abort(404)
        else:
            students_info.remove(student[0])
        return students_info


students_api = Blueprint('resources.Students', __name__)
api = Api(students_api)
api.add_resource(
      StudentList,
      '/api/v1/students',
      endpoint='students'
)

api.add_resource(
      Student,
      '/api/v1/student/<int:student_id>',
      endpoint='student'
)