"""
Module uses web framework Flask to run a web UI for Suiter

@app.route('/home')
@app.route('/')
def home():
    Displays the home page accessible at '/' or '/home'

@app.route('/echo')
def echo():
    Simple exho request - check whether the server is up

@app.route('/help')
def help():
    Displays the Suiter guide page accessible at '/help'

@app.route('/api/v1/calculator', methods=["GET"])
def calculator():
    Basic calculator for testing purposes 
    http://127.0.0.1:5000/api/v1/calculator?operation=plus&num1=int&num2=int
"""


from flask import Flask, render_template
from flask_restful import fields, reqparse

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    """
    Displays the home page accessible at '/' or '/home'
    """
    return render_template("index.html")

@app.route('/echo')
def echo():
    """
    Simple exho request - check whether the server is up
    https://code-maven.com/echo-with-flask-and-python
    """
    return 'echo_reply'

@app.route('/help')
def help():
    """
    Displays the Suiter guide page accessible at '/help'
    """

@app.route('/api/v1/calculator', methods=["GET"])
def calculator():
    """
    Basic calculator for testing purposes 
    http://127.0.0.1:5000/api/v1/calculator?operation=plus&num1=int&num2=int
    """

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
        return 'Error: Operation is not supported', 400

    response = {"Result": result}
    return response, 200


if __name__ == "__main__":
    app.run(debug=True, port=3000)