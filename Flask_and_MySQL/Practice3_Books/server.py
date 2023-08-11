from flask_app import app
import flask_app.controllers.authors
import flask_app.controllers.books

if __name__=="__main__":
    app.run(debug=True)