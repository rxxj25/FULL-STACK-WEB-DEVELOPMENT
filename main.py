from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project1.db'
app.config['SECRET_KEY'] = 'bb9538ba3b3963bf447fa53ebd5d7fc6'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    password = db.Column(db.Text)
    gender = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    phone_no = db.Column(db.Integer, unique=True)
    address = db.Column(db.Text)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='admin', uselist=False)

class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    complaint_details = db.Column(db.Text)
    

    def __repr__(self):
        return f"Complaint(id={self.id}, complaint_details='{self.complaint_details}')"


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    address = TextAreaField('Address', validators=[DataRequired()])
    terms_agreed = BooleanField('Agree to terms and conditions', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class AdminForm(FlaskForm):
    id = StringField('ID Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ComplaintForm(FlaskForm):
    id = StringField('ID Number', validators=[DataRequired()])
    complaint_details = TextAreaField('Complaint Details', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template('main.html')

@app.route('/registration.html', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            password=form.password.data,
            gender=form.gender.data,
            email=form.email.data,
            phone_no=form.phone.data,
            address=form.address.data,
        )
        db.session.add(user)
        db.session.commit()
        flash('Registration successful', 'success')
        return redirect(url_for('home'))
    return render_template('registration.html', form=form)

@app.route("/userlogin.html", methods=['GET', 'POST'])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login successful', 'success')
        return redirect(url_for('user'))
    return render_template('userlogin.html', form=form)

@app.route("/commissionerlogin.html", methods=['GET', 'POST'])
def admin_login():
    form = AdminForm()
    if form.validate_on_submit():
        flash('Login successful', 'success')
        return redirect(url_for('admin'))
    return render_template('commissionerlogin.html', form=form)

@app.route("/user.html", methods=['GET', 'POST'])
def user():
    return render_template("user.html")

@app.route('/HOME', methods=['GET', 'POST'])
def home_page():
    return redirect(url_for('home'))

@app.route('/bill.html', methods=['GET', 'POST'])
def bill_page():
    return render_template('bill.html')



@app.route('/complaint.html', methods=['GET', 'POST'])
def submit_complaint():
    form = ComplaintForm()
    if form.validate_on_submit():
        id = form.id.data
        complaint_details = form.complaint_details.data

        new_complaint = Complaint(id=id,complaint_details=complaint_details)
        db.session.add(new_complaint)
        db.session.commit()
        flash('Complaint submitted successfully', 'success')
        return redirect(url_for('home'))
    return render_template('complaint.html', form=form)

@app.route("/admin.html", methods=['GET', 'POST'])
def admin():
    return render_template("admin.html")

@app.route('/camera.html', methods=['GET', 'POST'])
def cctv_page():
    return render_template('camera.html')

@app.route('/list.html', methods=['GET', 'POST'])
def complaint_list():
    complaints = Complaint.query.all()
    grouped_complaints = {}
    for complaint in complaints:
        id = complaint.id
        if id not in grouped_complaints:
            grouped_complaints[id] = [complaint]
        else:
            grouped_complaints[id].append(complaint)

    return render_template('list.html', grouped_complaints=grouped_complaints)


@app.route('/user_list.html', methods=['GET', 'POST'])
def user_list():
    users = User.query.all()
    return render_template('user_list.html', users=users)



if __name__ == '__main__':
    app.run(debug=True)
