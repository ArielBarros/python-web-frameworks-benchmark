import redis
from flask import Flask, request, render_template
from marshmallow import Schema, fields

app = Flask(__name__, template_folder='.')
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

@app.route('/template', methods=['GET'])
def template():
    return render_template('template.html', people=people)

@app.route('/database', methods=['POST'])
def database():
    data, errors = SimpleSchema.load(request.json)
    if not errors:
        value = r.get(data['key_name'])
        return value, 200

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

