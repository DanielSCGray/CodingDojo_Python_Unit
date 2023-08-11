from flask_app import app
from flask_app.models import student
from flask_app.controllers import students




if __name__=="__main__":
    app.run(debug=True)