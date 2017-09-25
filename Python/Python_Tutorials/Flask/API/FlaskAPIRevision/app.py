from flask import Flask

import models
from Resources.employee import employee_api

DEBUG = True
HOST = '127.0.0.1'
PORT = 8000

app = Flask(__name__)
app.register_blueprint(employee_api)


@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)