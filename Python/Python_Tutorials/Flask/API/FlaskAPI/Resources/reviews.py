from flask import jsonify, Blueprint

from flask_restful import Resource, Api, reqparse, inputs


class ReviewList(Resource):
    def __init__(self):
        self.repparse = reqparse.RequestParser()
        self.repparse.add_argument(
            'course',
            type=inputs.positive,
            required=True,
            help='No Course Provided',
            location=['forms', 'json']
        )
        self.repparse.add_argument(
            'rating',
            type=inputs.int_range(1,5),
            required=True,
            help='No Ratings Provided',
            location=['forms', 'json']
        )
        self.repparse.add_argument(
            'comment',
            required=False,
            nullable=True,
            location=['forms', 'json'],
            default=''
        )



    def get(self):
        return jsonify({'reviews': [{'course': 1, 'ratings': 5}]}) # converts the argument into Json response


class Review(Resource):
    def get(self, id):
        return jsonify({'course': 1, 'ratings':5})

    def put(self, id):
        return jsonify({'course': 1, 'ratings': 5})

    def delete(self, id):
        return jsonify({'course': 1, 'ratings': 5})


reviews_api = Blueprint('Resources.reviews', __name__)
api = Api(reviews_api)
api.add_resource(
    ReviewList,
    '/reviews',
    endpoint='reviews'
)

api.add_resource(
    Review,
    '/review/<int:id>',
    endpoint='review'
)