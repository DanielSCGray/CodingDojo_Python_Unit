from flask_app import app
from flask_app.models import email
from flask_app.controllers import emails




if __name__=="__main__":
    app.run(debug=True)