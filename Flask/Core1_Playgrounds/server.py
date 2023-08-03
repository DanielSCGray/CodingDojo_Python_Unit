from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def display():
    return render_template('index.html', x=3, newcolor='blue')

app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/play/<int:num>')
def display2(num):

    return render_template("index.html", x=num, newcolor='blue')

@app.route('/play/<int:num>/<user_color>')
def display3(num, user_color):
    return render_template("index.html", x=num, newcolor=user_color)






if __name__=="__main__":
    app.run(debug=True)