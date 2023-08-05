from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ea3fdb7f1bcf66419ab5eb540eecbc8dc82941cf7e073d49b4def6928d801f25'

@app.route('/')
def homepage():
    if 'real_count' not in session:
        session['real_count'] = 1
    else:
        session['real_count'] += 1
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def delete_session():
    session.clear()
    return redirect('/')

@app.route('/change', methods=['POST'])
def change():
    if request.form['change'] == '2':
        session['count'] += 1
        return redirect('/')
    elif request.form['change'] == 'reset':
        return redirect('/destroy_session')

@app.route('/user_num', methods=['POST'])
def user_increase():
    num = int(request.form['user_num'])
    session['count'] += num - 1
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)