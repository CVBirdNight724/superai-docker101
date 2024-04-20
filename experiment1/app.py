from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/home")
def hello_world():
    return "Hello My Home!"

if __name__ =="__main__":
    app.run(port=5000)