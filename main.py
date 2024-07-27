from flask import Flask, request, jsonify, abort
from flask_restful import reqparse
from flask_cors import CORS
from gpt_query import query
from var import response_example
from dotenv import load_dotenv
from objects import obj_error
import os
import json

load_dotenv()
app = Flask(__name__)
CORS(app)

allowed_token = 'token'


def verify_token(token):
    token = request.args.get("token")
    if (token != os.environ.get('TOKEN')):
        abort(401, "Unauthorized: Token inválido o no proporcionado")

@app.route("/")
def root():
    return "Not Found", 404

@app.route("/get-data/", methods=['GET'])
def get_data():
    city = request.args.get("city")
    token = request.args.get("token")
    if(token != os.environ.get('TOKEN')):
        abort(401, "Unauthorized: Token inválido o no proporcionado")
    days = request.args.get("days")
    # verify_token(token)
    if int(days) > 5:
        days = 5
    elif int(days) <= 0:
        return (jsonify(obj_error)) #error
    result = json.loads(query(city, days))
    return jsonify(result), 201



@app.route("/example/", methods=['GET'])
def example():
    token = request.args.get("token")
    if(token != os.environ.get('TOKEN')):
        abort(401, "Unauthorized: Token inválido o no proporcionado")
    return jsonify(response_example), 201

@app.route("/made/", methods=['GET'])
def made():
    token = request.args.get("token")
    if(token != os.environ.get('TOKEN')):
        abort(401, "Unauthorized: Token inválido o no proporcionado")
    with open('made.json') as f:
        data = json.load(f)
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True, port=8080)