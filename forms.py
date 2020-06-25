from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, Length


class SignupForm(FlaskForm):
    first_name = StringField('First Name', [DataRequired()])
    last_name = StringField('Last Name', [DataRequired()])
    email = StringField('Email', [Email(message=('Not a valid email address.')), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, message="Password must be 6 charecters or more.")])
    submit = SubmitField('Sign Up')
