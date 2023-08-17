from flask_app import app
from flask_app.models import user, message
from flask import redirect, render_template, request, session, flash


@app.route('/welcome')
def welcome_page():
    if 'user_id' not in session.keys():
        return redirect('/')
    current_user = user.User.get_with_messages(session['user_id'])
    num_recieved_messages = len(current_user.my_messages)
    messages_and_senders = current_user.recieved_mail_senders()
    messages_and_senders = sorted(messages_and_senders, key=lambda sender: sender[1].first_name)
    other_users = user.User.get_all()
    return render_template('welcome.html', user=current_user, recieved_messages=messages_and_senders, num_recieved_messages=num_recieved_messages, other_users=other_users)

@app.post('/send')
def send_messsage():
    message.Message.create(request.form)
    return redirect('/welcome')

@app.post('/delete/<int:message_id>')
def delete_message(message_id):
    message.Message.delete(message_id)
    return redirect('/welcome')