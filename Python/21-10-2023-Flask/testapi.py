from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route("/")
def show_form():
    return render_template("index.html")

@app.route("/userData",methods=['POST'])
def chk_password_post():
    user_name = request.form.get('username1')
    pass_word = request.form.get('password1')
    return f"hello {user_name} {pass_word} ! Thanks for the input"

@app.route("/userData",methods=['GET'])
def chk_password_get():
    user_name = request.args.get('username1')
    pass_word = request.args.get('password1')
    return f"hello {user_name} {pass_word} ! Thanks for the input"

if __name__ == "__main__":
    app.run(host="0.0.0.0")