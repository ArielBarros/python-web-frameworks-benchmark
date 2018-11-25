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
# @app.route('/database', method='GET')
def database():
	# return bottle.BaseRequest.json
	return "banco de dados"
  #   data, errors = SimpleSchema.load(bottle.BaseRequest.json)
  #   if not errors:
  #       value = r.get(data['key_name'])
  #       # return value # ver isso roda de boa
		# return "banco de dados"

@app.route('/')
def hello():
    return "Hello World!"

# run(host='0.0.0.0', port=5000, debug=True)

