from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    first_name = StringField('First Name', [DataRequired("Please enter first name.")])
    last_name = StringField('Last Name', [DataRequired("Please enter last name.")])
    email = StringField('Email', [Email(message=('Not a valid email address.')), DataRequired("Please enter email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please choose a password."), Length(min=6, message="Password must be 6 charecters or more.")])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', [Email(message=('Not a valid email address.')), DataRequired("Please enter email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a Password.")])
    submit = SubmitField("Sign in")
