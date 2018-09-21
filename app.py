from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Brian"

@app.route('/hithere')
def hi_there_everyone():
    return "I just hit /hithere"

@app.route('/bye')
def bye():
    c = 2*534
    s = str(c)
    return "bye " + s

if __name__ == "__main__":
    app.run(debug=True)
