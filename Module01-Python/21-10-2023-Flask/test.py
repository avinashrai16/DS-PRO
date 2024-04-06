
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def home():
    return f"""<h1>Hello, and welcome to Flask setup!</h1> 
           click on below avilable function 
           </br>
           1. <a href = "/add">add </a></br>
           2. <a href = "/avinash">avinash</a></br>
           3. <a href = "/getUser">getUser</a></br>
    """

@app.route("/add",methods=['GET'])
def addition ():
    print(10+6)
    return f" test return"

@app.route("/avinash")
def print_name ():
    return "<h1>Hello, Avinash!</h1>"

@app.route("/getUser")
def print_user():
    data = request.args.get("name")
    return f"{data}"

if __name__ == "__main__":
    app.run(host="0.0.0.0")