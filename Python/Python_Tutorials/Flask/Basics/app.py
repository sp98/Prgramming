from flask import Flask
from flask import render_template
from flask import request  # request is a global object and is available everywhere.

app = Flask(__name__)

# fetching arguments sent by the user using request library
# @app.route('/')
# def index(name='Santosh'):
#     name = request.args.get('name', name)
#     return 'Hello Flask! From {}'.format(name)


@app.route('/')
@app.route('/<name>')
def index(name='Santosh'):
    return render_template('index.html', name=name)


# we can decide the type of arguments send by the user as well.
# we get 404 if the arguments do not match.
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')

def add(num1, num2):
    context = { 'num1': num1, 'num2': num2}
    return render_template('add.html', **context )
    return '{} + {} = {}'.format(num1, num2, num1+num2)
    # the return type can't be an int. It has to be a String.


app.run(debug=True, port=8080, host='127.0.0.1')
