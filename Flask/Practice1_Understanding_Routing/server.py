from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def hi_name(name):
    return 'Hi ' + name

@app.route('/repeat/<int:num>/<string:word>')
def repeater(num, word):
    return f"{word * num}"

@app.route('/<command>')
def no_response(command):
    commsArray = ['dojo', 'say', 'repeat']
    if command:
        if command not in commsArray:
            return 'Sorry! No response. Try again.'
        
if __name__=="__main__":
    app.run(debug=True)