import os
from flask import Flask, render_template, session, redirect, url_for
from forms import  AddForm , DelForm
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app= Flask(__name__, template_folder='templates')
app.config['SECRET_KEY']='XXXXXXXXXXXXXXXXXXX'
############################################

        # SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    email = db.Column(db.String)


    def __init__(self,name,email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User name: {self.name} email: {self.email}"

############################################

        # VIEWS WITH FORMS

##########################################


@app.route('/are_you', methods=['GET', 'POST'])
def arm():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        # Add new user to database
        new_user = User('name','email')
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('base'))
    return render_template('arm.html',form=form)

GoogleMaps(app, key="API_KEY")
@app.route('/map', methods=["GET"])
def my_map():
    mymap = Map(
                identifier="view-side",
                varname="mymap",
                style="height:720px;width:1100px;margin:0;", # hardcoded!
                lat=37.4419, # hardcoded!
                lng=-122.1419, # hardcoded!
                zoom=15,
                markers=[(37.4419, -122.1419)] # hardcoded!
            )
    return render_template('example.html', mymap=mymap)

@app.route('/react')
def React_tools():
    return render_template("index.html", token="hello flask + react")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/')
def base():
 return render_template('base.html')


@app.route('/home')
def home():
 return render_template('home.html')


if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(debug=True, port=port)
