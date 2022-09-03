import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import  datetime

DB_HOST = os.getenv('DB_HOST', "localhost")
DB_USER = os.getenv('DB_USER', "app")
DB_PASS = os.getenv('DB_PASS', "Lw8KhGmn")
DB_NAME = os.getenv('DB_NAME', "demo")
AUTH_TOKEN = os.getenv('AUTH_TOKEN', "eyJzdWIiOiIxMjM0NTY3ODkwIiwibm")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Registration(db.Model):
    __tablename__ = "registration"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    email = db.Column(db.String(500))
    create = db.Column(db.DateTime)

    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.create = datetime.now()

class RegistrationSchema(ma.Schema):
    class Meta:
        fields = ("name", "email")

class RegistrationsSchema(ma.Schema):
    class Meta:
        fields = ("id","name", "email", "create")

registration_schema = RegistrationSchema()
registrations_schema = RegistrationsSchema(many=True)

@app.route('/registrations', methods = ['GET'])
def index():
    auth_header = request.headers.get('Authorization')

    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''
    if auth_token == AUTH_TOKEN:
        all_registrations = Registration.query.all()
        return jsonify(registrations_schema.dump(all_registrations))
    else:
        return {"message": "Access denied"}, 400

@app.route('/registrations', methods = ['POST'])
def create_registration():
    name = request.json.get('name', 'NA')
    email = request.json.get('email', 'NA')
    if name == "NA" or email == "NA":
        return {"message": "No input data provided"}, 400
    else:
        registration = Registration(name=name, email=email)
        db.session.add(registration)
        db.session.commit()
        return registration_schema.jsonify(registration)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=False)
