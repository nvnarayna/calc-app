from flask import Flask,render_template,request,jsonify

def calculator(a,b,operation):

  if (a.isnumeric() & b.isnumeric()):
    a=float(a)
    b=float(b)
    if operation == "add":
      result = a + b
    elif operation == "subtract":
      result = a - b
    elif operation == "divide":
      result = a / b
    elif operation == "multiply":
      result = a * b
    else:
      result = "Operations supported: add, subtract, divide, multiple only"
    
  else:
    result = "Please enter a valid number for a & b"
    

  return result

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
    a=request.form['a']
    op=request.form['op']
    b=request.form['b']
    return render_template('index.html',result=str(calculator(a,b,op)))


if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)
