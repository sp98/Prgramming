from flask import Flask
import models
from Resources.courses import courses_api
from Resources.reviews import reviews_api

app = Flask(__name__)
app.register_blueprint(courses_api)
app.register_blueprint(reviews_api, url_prefix='/api/v1')


@app.route('/')
def index():
    return "Welcome to Flask Learning!"

if __name__ == "__main__":
    models.initialize()
    app.run(debug=True)
