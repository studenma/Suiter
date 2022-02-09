"""
Module uses web framework Flask to run a web application for Suiter

@app.route('/api/v1/calculator', methods=["GET"])
def calculator():
    Basic calculator for testing purposes 
    http://127.0.0.1:5000/api/v1/calculator?operation=plus&num1=int&num2=int
"""

from flask import Flask, render_template, request, jsonify
from flask_restful import fields, reqparse
from flask_cors import CORS, cross_origin
from flask_swagger_ui import get_swaggerui_blueprint
import json
import yaml

import os,sys,inspect
# from suiter.suiter import generate_test_suite
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from suiter import logging

app = Flask(__name__)
cors = CORS(app)

calculator_operation = "add"

app.config['CORS_HEADERS'] = 'Content-Type'


SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI
API_URL = 'http://127.0.0.1:5000/api/v1/calculator/swagger.yaml'

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)


@app.route('/api/v1/calculator', methods=['GET', 'POST'])
def calculator():
    """
    Basic calculator for testing purposes 
    http://127.0.0.1:5000/api/v1/calculator?operation=plus&num1=int&num2=int
    """
    logging.debug(request)
    logging.debug(request.data)
    
    calculator_fields = {
        'operation': fields.String,
        'num1': fields.Integer,
        'num2': fields.Integer
    }

    calculator_args = reqparse.RequestParser()
    calculator_args.add_argument("operation", type=str, help="Operation is required", required=True)
    calculator_args.add_argument("num1", type=int, help="Two numbers are required", required=True)
    calculator_args.add_argument("num2", type=int, help="Two numbers are required", required=True)

    args = calculator_args.parse_args()
    operation = args["operation"]
    num1 = args["num1"]
    num2 = args["num2"]

    if operation == "add":
        result = num1 + num2
    elif operation == "substract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2
    else:
        return { 'Error': 'Operation is not supported'}, 400

    response = {"Result": result}
    return response, 200

@app.route('/api/v1/stateCalculator/viewOperation', methods=['GET'])
def viewOperation():
    """
    View operation of API calculator
    http://127.0.0.1:5000/api/v1/stateCalculator/viewOperation
    """
    response = {"Result": calculator_operation}
    return response, 200

@app.route('/api/v1/stateCalculator/changeOperation', methods=['GET'])
def changeOperation():
    """
    Change operation of API calculator
    http://127.0.0.1:5000/api/v1/stateCalculator/changeOperation
    """
    change_operation_arg = reqparse.RequestParser()
    change_operation_arg.add_argument("operation", type=str, help="Operation is required", required=True)

    args = change_operation_arg.parse_args()
    operation = args["operation"]

    global calculator_operation
    
    if operation in ['add', 'substract', 'multiply', 'divide']:
        calculator_operation = operation
    else:
        return { 'Error': 'Operation is not supported'}, 400
    
    str_response = "Operation changed to " + calculator_operation
    response = {"Result": str_response}
    return response, 200 

@app.route('/api/v1/stateCalculator', methods=['GET'])
def stateCalculator():
    """
    Calculator for API testing purposes - testing the API with states
    http://127.0.0.1:5000/api/v1/stateCalculator?&num1=int&num2=int
    """
    logging.debug(request)
    logging.debug(request.data)
    
    calculator_fields = {
        'operation': fields.String
    }

    calculator_args = reqparse.RequestParser()
    calculator_args.add_argument("num1", type=int, help="Two numbers are required", required=True)
    calculator_args.add_argument("num2", type=int, help="Two numbers are required", required=True)

    args = calculator_args.parse_args()
    num1 = args["num1"]
    num2 = args["num2"]


    if calculator_operation == "add":
        result = num1 + num2
    elif calculator_operation == "substract":
        result = num1 - num2
    elif calculator_operation == "multiply":
        result = num1 * num2
    elif calculator_operation == "divide":
        result = num1 / num2
    else:
        return 'Error: Calculator operation is not supported', 400

    response = {"Result": result}
    return response, 200

if __name__ == "__main__":
    app.run(debug=True)