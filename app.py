from bottle import route, run, template, static_file, error, BaseTemplate
import bottle
from models import *

app = bottle.default_app()
BaseTemplate.defaults['get_url'] = app.get_url

@route('/static/css/<filename:re:.*\.css>')
def css(filename):
    return static_file(filename, root='static/css')

@route('/static/js/<filename:re:.*\.js>')
def js(filename):
    return static_file(filename, root='static/js')

@route('/static/images/<filename:re:.*\.jpeg>')
def jpg_images(filename):
    return static_file(filename, root='static/images')

@route('/static/images/<filename:re:.*\.png>')
def png_images(filename):
    return static_file(filename, root='static/images')



@route('/', name='index')
def index():
    return template('index')


@route('/destination', name='destination')
def destination():
    return template('destination')


app.run(host='localhost', port=9988, reloader=True)

