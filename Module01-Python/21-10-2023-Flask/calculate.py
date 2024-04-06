from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def show_form():
    return render_template("calculate.html")

@app.route("/doMath",methods=['post'])
def chk_and_do_operation():
    operation_name = request.form['operation']
    result = 0
    try:
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(operation_name == 'add'):
            result = num1+num2
        elif(operation_name == 'subtract'):
            result = num1-num2
        elif(operation_name == 'multiply'):
            result = num1*num2
        elif(operation_name == 'divide'):
            result = num1/num2
        else:
            return f"operation could not processed at this time"
        
    except Exception as e:
        print(f"An exception occurred: {e}")
        return f"""Invalid input. Please provide valid numbers. <a href = "/"> Try again </a>"""
    
    return f"""<h3>the result of <u><i>{operation_name}</u></i> on <u><i>{num1}</u></i> and <u><i>{num2}</u></i> is : <u><i>{result}</u></i> </h3>
    <a href = "/"> Try again </a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0")