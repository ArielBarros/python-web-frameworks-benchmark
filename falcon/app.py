import falcon
import redis
import jinja2
import os
from marshmallow import Schema, fields

r = redis.StrictRedis(host='redis', port=6379, db=0)
r.set('1', 'hello world')

class SimpleSchema(Schema):
    key_name = fields.String()

SimpleSchema = SimpleSchema()

class Person: 
    def __init__(self, firstname, lastname, age, city): 
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.city = city

people = [Person('Marcos', 'Carlos', 30, 'Fortaleza'),
Person('Pedro', 'Andrade', 24, 'Belo Horizonte'),
Person('Francisco', 'Peixoto', 46, 'Rio de Janeiro'),
Person('Lara', 'Lima', 19, 'Porto Alegre'),
Person('Regina', 'Soares', 22, 'Recife')]

root_path = os.path.dirname(os.path.abspath(__file__))
loader = jinja2.FileSystemLoader(root_path)
env = jinja2.Environment(loader=loader)

class Hello(object):
    def on_get(self, req, resp):
        resp.body = 'Hello World!'

class Template(object):
    def on_get(self, req, resp):
        template = env.get_template('template.html')
        resp.set_header('Content-Type', 'text/html')
        resp.body = template.render(people=people)

class Database(object):
    def on_post(self, req, resp):
        data, errors = SimpleSchema.loads(req.stream.read().decode('utf-8'))
        if not errors:
            value = r.get(data['key_name'])
            resp.body = value

app = falcon.API()
app.add_route('/', Hello())
app.add_route('/template', Template())
app.add_route('/database', Database())
