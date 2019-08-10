from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
##
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError


class AddForm(FlaskForm):

    name = StringField('Name:')
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Post')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of user to Remove:')
    submit = SubmitField('Remove user')
