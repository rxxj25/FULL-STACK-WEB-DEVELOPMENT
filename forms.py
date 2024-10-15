from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField,TextAreaField
from wtforms.validators import DataRequired,Length,EqualTo
from flask import Flask,render_template,url_for
from wtforms.validators import Email as EmailValidator

app=Flask(__name__)
app.app_context().push()
class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), EmailValidator()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    address = TextAreaField('Address', validators=[DataRequired()])
    terms_agreed = BooleanField('Agree to terms and conditions', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), EmailValidator()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class AdminForm(FlaskForm):
    id = StringField('ID Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), EmailValidator()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ComplaintForm(FlaskForm):
    id = StringField('ID Number', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email Address', validators=[DataRequired(), EmailValidator()])
    complaint_details = TextAreaField('Complaint Details', validators=[DataRequired()])
    submit = SubmitField('Submit')
   