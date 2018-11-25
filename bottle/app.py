import bottle
import redis
from marshmallow import Schema, fields

app = bottle.Bottle()
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

@app.route('/template')
def template():
    return bottle.template('template', people=people)

@app.route('/database', method='POST')
def database():
    data, errors = SimpleSchema.load(bottle.request.json)
    if not errors:
        value = r.get(data['key_name'])
        return value

@app.route('/')
def hello():
    return "Hello World!"

bottle.debug(True)
