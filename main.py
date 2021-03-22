from flask import Flask

app = Flask(__name__)

@app.route('/')
def base_route():
    return "hello world"

#@app.route('/hello/<name>')
#def hello(name):
 #   return f"hello {name}"

#@app.route('/hello/<float:number>')
#def hello(number):
 #   return f"hello {number}"

#@app.route("/hello/<float:number>")
#def hello(number):
 #   if number <= 10:
 #       return f"hello {number}", 200 # status code
 #   if number >= 11:
 #       return f"hello {number}", 206 # partial content -> 206 status code

@app.route("/hello/<float:number>", methods=["POST"])
def hello(number):
    if number <= 10:
        return f"hello {number}", 200 # status code
    if number >= 11:
        return f"hello {number}", 206 # partial content -> 206 status code

if __name__=="__main__":
    app.run( debug=True)