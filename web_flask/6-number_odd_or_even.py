#!/usr/bin/python3
""" A script that will start a Flask web app """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Functiono to display item """
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
    """ Fuunction to display Python, followed by value of text variable """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ Function to display n """
    return '{} is number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Function to display HTML page only if n is an integer """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ Function to display if number is even or odd """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000)
