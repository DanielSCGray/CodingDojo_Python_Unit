from flask_app import app
# from flask_app.models import user
from flask_app.controllers import main




if __name__=="__main__":
    app.run(debug=True)