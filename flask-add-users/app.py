# 'Add users to the database' demo app on Python and Flask
# Programming language version: Python 3.6.9
# Developer: Valeriy B.

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app_title = "Add Users App"


# Creating models for adding user to the database
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	def __repr__(self):
		return f"User {self.id}"


# Routing for index page
@app.route('/', methods=["POST", "GET"])
def index():
	if request.method == "POST":
		if request.form['fname'] == "":
			first_name = "First name: Blank"
		else:
			first_name = request.form['fname'].title()
		if request.form['lname'] == "":
			last_name = "Last name: Blank"
		else:
			last_name = request.form['lname'].title()
		user = User(first_name=first_name, last_name=last_name)
		db.session.add(user)
		db.session.commit()
		users = User.query.all()
		return render_template('index.html', app_title=app_title, users=users)
	else:
		users = User.query.all()
		return render_template('index.html', app_title=app_title, users=users)


# Routing for updating user information
@app.route('/update/<int:id>', methods=['POST', 'GET'])
def user_update(id):
	if request.method == "POST":
		updated_user = User.query.get_or_404(id)
		updated_user.first_name = request.form['fname']
		updated_user.last_name = request.form['lname']
		db.session.commit()
		return redirect(url_for('index'))
	else:
		user_to_update = User.query.get_or_404(id)
		return render_template('update.html', user=user_to_update)


# Routing for deleting a user from the database
@app.route('/del/<int:id>')
def user_delete(id):
	user_to_delete = User.query.get_or_404(id)
	db.session.delete(user_to_delete)
	db.session.commit()
	return redirect(url_for('index'))
	

if __name__ == '__main__':
	app.run(debug=True)
