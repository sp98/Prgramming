from flask_restful import (Resource, reqparse, Api,
                           reqparse, inputs, fields,
                           marshal, marshal_with, abort)

from flask import jsonify, Blueprint

import models

employee_response = {
  'employee_id': fields.String,
  'name': fields.String,
  'skills': fields.String,
  'experience': fields.Integer
}


def employee_or_404(employee_id):
    try:
        employee = models.Employee.get(models.Employee.employee_id == employee_id)
        print(employee)
    except models.Employee.DoesNotExist:
        abort(400)
    else:
        return employee


class EmployeeList(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument(
            'employee_id',
            required=True,
            help='No employee ID Provided',
            location=['form', 'json'])
        # where to look in the request for data. Which ever comes last is looked into first
        self.reqparser.add_argument(
            'name',
            required=True,
            help='No employee name Provided',
            location=['form', 'json'])
        self.reqparser.add_argument(
            'skills',
            required=True,
            help='No employee skills Provided',
            location=['form', 'json'])
        self.reqparser.add_argument(
            'experience',
            required=True,
            help='No employee experience Provided',
            location=['form', 'json'],
            type=inputs.positive
        )
        super().__init__()  # whey did we use this?

    def get(self):

        employees = [marshal(employee, employee_response)
                     for employee in models.Employee.select()]
        # return {'employees': employees}
        # we can turn this into json seriazale so this will give error
        return {'employees': employees}

    def post(self):
        args = self.reqparser.parse_args()  # to parse the args on post method.
        models.Employee.create(**args)
        return jsonify({'method': 'post'})


class Employee(Resource):
    def get(self, employee_id):
        return marshal(employee_or_404(employee_id), employee_response)

    def put(self, employee_id):
        args = self.reqparse.parse_args()  # to parse the request args in put method
        query = models.Employee.update(**args).where(models.Employee.employee_id == employee_id)
        query.execute()
        return models.Employee.select().where(models.Employee.employee_id == employee_id)


employee_api = Blueprint('Resources.employee', __name__)
api = Api(employee_api)
api.add_resource(
    EmployeeList,
    '/api/v1/employees',
    endpoint='employees'
)
api.add_resource(
    Employee,
    '/api/v1/employees/<string:employee_id>',
    endpoint='employee'
)

