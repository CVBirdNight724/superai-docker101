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

@app.route("/avg", methods=['POST'])
def average_number():
    json_body = request.json
    
    """
    Your AI Model
    """
    
    if "data" in json_body:
    
        return { 
            "status": True,
            "result": sum(json_body["data"])
        }
    
    else:
        return {
            "status": False,
            "content": "Wrong Format"
        }
    
if __name__ =="__main__":
    app.run(port=5000)