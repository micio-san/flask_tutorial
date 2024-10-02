from flask import Flask, request, make_response

app=Flask(__name__)


@app.route("/")

def get_homepage():
    return '<h1>HIII</h1>'

@app.route("/hello", methods=["GET", "POST"])

def get_():
    response=make_response("Hiiiiiii")
    response.status_code=202
    response.headers["content-type"]="text/plain"
    return response
    

@app.route("/greet/<name>")

def greet_someone(name):
    return f"Hello, {name}"

#you need to typecast from string to int to execute an operation
@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"{number1} + {number2}={number1 + number2}"

@app.route("/handle_url_param")
#return an empty dictionary
def handle_params():
    if "greeting" in request.args.keys() and "name" in request.args.keys():
       greeting=request.args.get("greeting")
       name=request.args.get("name")
       return f"{greeting} {name}!"
    else:
        return "Hi!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)