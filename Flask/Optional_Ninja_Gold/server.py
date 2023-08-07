from datetime import datetime
from random import randint

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'eafdb7f1bcf66419ab5eb540eecbc8dc82941cf7e073d49b4def6928d801f25'


@app.route('/')
def homepage():
    if 'gold_total' not in session.keys():
        session['gold_total'] = 0
    
    if 'activity_data' not in session.keys():
        print('not found')
        session['activity_data'] = []

    print(session['activity_data'])
    return render_template('index.html')

@app.route('/process', methods=['POST', 'GET'])
def process():
    if request.form['form_id'] == 'farm':
        print('yes')
        gold = randint(10,20)
        session['gold_total'] += gold
        session['activity_data'] += [assembler('Farm', gold)]
    elif request.form['form_id'] == 'cave':
        gold = randint(5,10)
        session['gold_total'] += gold
        session['activity_data'] += [assembler('Cave', gold)]
    elif request.form['form_id'] == 'house':
        gold = randint(2,5)
        session['gold_total'] += gold
        session['activity_data'] += [assembler('House', gold)]
    elif request.form['form_id'] == 'casino':
        gold = randint(-50,50)
        session['gold_total'] += gold
        session['activity_data'] += [assembler('Casino', gold)]
    elif request.form['form_id'] == 'reset':
        session.clear()

    return redirect('/')

def assembler(location, num):
    
    if num < 0:
        is_pos = False
    else:
        is_pos = True
    date = datetime.now()
    gold_amt = abs(num) # may need an str convert
    return [is_pos, location, gold_amt, date]


if __name__=="__main__":
    app.run(debug=True)