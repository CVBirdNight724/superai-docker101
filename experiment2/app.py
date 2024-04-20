from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/home")
def home():
    return "Hello My Home!"

@app.route("/sum", methods=['GET'])
def sum_number():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    return {
        "result": float(num1) + float(num2)
    }

if __name__ =="__main__":
    app.run(port=5000)