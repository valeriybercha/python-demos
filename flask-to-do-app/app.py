# Flask demo application for register and login users

from flask import Flask, render_template, url_for, redirect, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo, ValidationError
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)


# Load user object
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)


####### FORMS SECTION - forms.py ########

# User database model
class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(50), unique=True, nullable=False)
	name = db.Column(db.String(120), nullable=False)
	password = db.Column(db.String(20), nullable=False)
	tasks = db.relationship('Task', backref="user")

	def __repr__(self):
		return f'User {self.id} - {self.name} - {self.email} - {self.task}'


# Task database model
class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	task = db.Column(db.String(250), nullable=False)
	task_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	task_completed = db.Column(db.Boolean(), nullable=False, default=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return f'Task {self.id} - {self.task} - {self.task_added} - {self.task_completed} - {self.user_id}'


# User registration form validation
class UserRegistration(FlaskForm):
	email = StringField('Email', validators=[InputRequired(), Email(), Length(min=4, max=50)])
	name = StringField('Full Name', validators=[InputRequired(), Length(min=5, max=120)]) 
	password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=20)])
	confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('This email already exists in the database. Try another one')


# User login form validation
class UserLogin(FlaskForm):
	email = StringField('Email', validators=[InputRequired(), Email()])
	password = PasswordField('Password', validators=[InputRequired()])
	submit = SubmitField('Sign In')


# Task form validation
class TaskAdd(FlaskForm):
	task = StringField('Add a task', validators=[InputRequired(), Length(max=250)])
	submit = SubmitField('Add task')


######## ROUTING SECTION - routes.py ########

# Routing for 'home/add a task' function
@app.route('/', methods=["GET", "POST"])
def index():
	form = TaskAdd()
	if form.validate_on_submit():
		task_to_add = Task(task=form.task.data, user=current_user)
		db.session.add(task_to_add)
		db.session.commit()
		return redirect(url_for('index'))
	else:
		curr_user_id = current_user.get_id()
		tasks = Task.query.filter(Task.user_id==curr_user_id).filter_by(task_completed=True).all()
	return render_template('index.html', form=form, tasks=tasks)


# Routing for 'register' function
@app.route('/register', methods=["GET", "POST"])
def register():
	form  = UserRegistration()
	if form.validate_on_submit():
		user_to_register = User(email=form.email.data.lower(), name=form.name.data.title(), password=generate_password_hash(form.password.data))
		db.session.add(user_to_register)
		db.session.commit()
		return redirect(url_for('login'))
	return render_template('register.html', form=form)


# Routing for 'login' function
@app.route('/login', methods=["GET", "POST"])
def login():
	form = UserLogin()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and check_password_hash(user.password, form.password.data):
			login_user(user)
			return redirect('success')
		else:
			flash('Incorrect email or password. Please try again')
	return render_template('login.html', form=form)


# Routing for 'logout' function
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))


# Routing for 'about' function
@app.route('/about')
def about():
	return render_template('about.html')


# Routing for task 'done' function
@app.route('/done/<int:task_id>')
def task_done(task_id):
	done_task = Task.query.get_or_404(task_id)
	done_task.task_completed = False
	db.session.commit()
	return redirect(url_for('index'))


# Routing for task 'complete/done' function
@app.route('/completed')
@login_required
def completed_tasks():
	curr_user_id = current_user.get_id()
	tasks = Task.query.filter(Task.user_id==curr_user_id).filter_by(task_completed=False).all()
	return render_template('completed.html', tasks=tasks)


# Routing for task 'update' function
@app.route('/update/<int:task_id>', methods=["GET", "POST"])
@login_required
def task_update(task_id):
	task_to_update = Task.query.get_or_404(task_id)
	if request.method == "POST":
		task_to_update.task = request.form['task']
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('update-task.html', task_to_update=task_to_update)


# Rounting for task 'delete' function from home page
@app.route('/delete/<int:task_id>')
@login_required
def task_delete(task_id):
	task_to_delete = Task.query.get_or_404(task_id)
	db.session.delete(task_to_delete)
	db.session.commit()
	return redirect(url_for('index'))


# Routing for task 'delete' function from completed tasks page
@app.route('/deletec/<int:task_id>')
@login_required
def task_delete_complete(task_id):
	task_to_delete = Task.query.get_or_404(task_id)
	db.session.delete(task_to_delete)
	db.session.commit()
	return redirect(url_for('completed_tasks'))


# Routing for task 'undone' function from completed tasks page
@app.route('/undone/<int:task_id>')
@login_required
def task_undone(task_id):
	undone_task = Task.query.get_or_404(task_id)
	undone_task.task_completed = True
	db.session.commit()
	return redirect(url_for('completed_tasks'))


# TEST Routing for 'success' function
@app.route('/success')
def success():
	return render_template('test-success.html') 


# TEST Rouiting for 'users' function
@app.route('/users')
@login_required
def users():
	users = User.query.all()
	return render_template('test-users.html', users=users)


if __name__ == "__main__":
	app.run(debug=True)
