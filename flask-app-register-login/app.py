# Basic app registration app created with Flask, Flask-SQLAlchemy, Flask-WTForms
# The app was created in WSL (Windows Subsystem for Linux) environment using the Nano editor

from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from flask_login import LoginManager, UserMixin, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "your_secret_key"

db = SQLAlchemy(app)
login_manager = LoginManager(app)


################ FORMS SECTION - forms.py ###############

# Creating models for user registration for FLask-SQLALchemy
class UserRegistration(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	fullname = db.Column(db.String(120), nullable=False)
	email = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(20), nullable=False)

	def __repr__(self):
		return f'User({self.username}, {self.fullname}, {self.email})'


# User registration form validation with Flask-WTForms
class UserForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
	fullname = StringField('Full Name', validators=[DataRequired(), Length(min=4, max=120)])
	email = StringField('Email', validators=[DataRequired(), Email(), Length(min=5, max=50)])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
	confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

	def validate_username(self, username):
		form= UserForm()
		check_username = UserRegistration.query.filter_by(username=form.username.data).first()

		if check_username:
			raise ValidationError("This username already exists. Choose another one")

	def validate_email(self, email):
		form = UserForm()
		check_email = UserRegistration.query.filter_by(email=form.email.data).first()
		if check_email:
			raise ValidationError("This email already exists. Go to Login page")


# User login form validation with Flask-WTForms
class UserLogin(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')


################ ROUTING SECTION - routes.py ###################

# Creating login manager session
@login_manager.user_loader
def load_user(user_id):
	return UserRegistration.query.get(user_id)


# Routing for 'index/registartion' page with form for user registration
@app.route('/', methods=["POST", "GET"])
def index():
	form = UserForm()
	if form.validate_on_submit():
		user_to_register = UserRegistration(username=form.username.data.lower(), fullname=form.fullname.data.title(), email=form.email.data.lower(), password=generate_password_hash(form.password.data))
		db.session.add(user_to_register)
		db.session.commit()
		return render_template('success.html', message="Register")
	return render_template('index.html', form=form)


# Routing for 'login' function
@app.route('/login', methods=["GET", "POST"])
def login():
	form = UserLogin()
	if form.validate_on_submit():
		user = UserRegistration.query.filter_by(email=form.email.data).first()
		if user and check_password_hash(user.password, form.password.data):
			login_user(user)
			return render_template('success.html', message="Login")
		else:
			flash('Incorrect login or password. Try again')
	return render_template('login.html', form=form)


# Routing for 'logout' function
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))


# Routing for displaying all users
@app.route('/users')
def users():
	users = UserRegistration.query.all()
	return render_template('users.html', users=users)


# Routing for 'success' function
@app.route('/success')
def success():
	return render_template('success.html')


if __name__ == '__main__':
	app.run(debug=True)
