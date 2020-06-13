

from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        return jsonify('Welcome wanderers!!')


class Recommend(Resource):

    def get_ml_op(self, user_email_id, user_location):
        user_location = eval(user_location)
        resp = {'Email': user_email_id,
                'Latitude': user_location[0],
                'Longitude': user_location[1]}
        return resp

    def get(self):
        args = request.args
        email = args.get('email')
        location = args.get('location')
        resp = self.get_ml_op(email, location)
        return jsonify(resp)

    def post(self):
        # Currently no action on POST request, Return received body
        data = request.get_json()
        return jsonify({'data': data}), 201


# Map resources to URLs
api.add_resource(Home, '/')
api.add_resource(Recommend, '/recommend/')

if __name__ == '__main__':
    app.run(debug=True)
