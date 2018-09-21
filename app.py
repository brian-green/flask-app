# Note new modules!
from flask import Flask, jsonify, request
app = Flask(__name__)

#127.0.0.1:5000/
@app.route('/')
def hello_world():
    return "Hello Brian"

@app.route('/hithere')
def hi_there_everyone():
    return "I just hit /hithere!"

@app.route('/add_two_num', methods=["POST","GET"])
def add_two_nums():
    # Get x,y from the post data
    data = request.get_json()
    x = data["x"]
    y = data["y"]

    # Add x,y
    z = x + y

    # Prepare JSON
    json = {"z":z}

    # Return JSON to client
    return jsonify(json)

@app.route('/bye')
def bye():
    c = 2*534
    s = str(c)
    return "bye " + s

if __name__ == "__main__":
    app.run(debug=True)
