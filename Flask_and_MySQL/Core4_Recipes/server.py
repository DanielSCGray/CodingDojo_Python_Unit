from flask_app import app
from flask_app.models import user, recipe
from flask_app.controllers import users, recipes1




if __name__=="__main__":
    app.run(debug=True)