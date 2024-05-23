#!/usr/bin/python3
"""A script that startsup a web application (flask)"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Function to print stuff"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Function to display another stuff"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Function to display C followed by value of text variable"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
