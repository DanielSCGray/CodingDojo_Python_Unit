from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html', x=8, y=8, color1='red', color2='black')

@app.route('/<int:num1>')
def one_num(num1):
        return render_template('index.html', x=num1, y=8, color1='red', color2='black')


@app.route('/<int:num1>/<int:num2>')
def two_num(num1, num2):
        return render_template('index.html', x=num1, y=num2, color1='red', color2='black')

@app.route('/<int:num1>/<int:num2>/<color1>/<color2>')
def full_customization(num1, num2, color1, color2):
        return render_template('index.html', x=num1, y=num2, color1=color1, color2=color2)





if __name__=="__main__":
    app.run(debug=True)