from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/home")
def home():
    return "Hello My Home!"

if __name__ =="__main__":
    app.run(port=5000)
