from flask import Flask,request,jsonify,render_template
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


     
@app.route('/calculate', methods=['GET','POST'])
def calculate():
    operation = request.json['operation']
    number1 = int(request.json['number1'])
    number2 = int(request.json['number2'])

    if operation == 'add':
        result = number1 + number2
        return jsonify({"result": result})
    elif operation == 'subtract':
        result = number1 - number2
        return jsonify({"result": result})
    elif operation == 'multiply':
        result = number1 * number2
        return jsonify({"result": result})
    elif operation == 'divide':
        result = number1 / number2
        return jsonify({"result": result})
    else:
        return "Invalid Operation"
     
    



