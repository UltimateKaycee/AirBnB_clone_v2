#!/usr/bin/python3
""" A script to start a web application (Flask) """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Function to display item """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Function to display another item """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ Function to display C followed by value of text variable """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """ Function to display Python, followed by value of text variable,
    The default value is: is cool """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ Function to display n """
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
