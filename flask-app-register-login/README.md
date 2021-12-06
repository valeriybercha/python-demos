# User registration and login app with Flask, Flask-SQLAlchemy, Flask-WTForms and Flask-Login

### Features:
- Register a user to the database:
	- Registration form fields and fields validation:
		- Username (Unique, Length: 4 - 20)
		- Full Name (Length: 4 - 120)
		- Email (Unique, Length: 5 - 50)
		- Password (Length: 8 - 20)
		- Confirm password (EqualTo: password)
- Verification if username or email already exists in the database when registering a new user
- Login into the system for registered users:
	- Login form fields:
		- Email (Required)
		- Password (Required)
- Successfull message display when users are registered or logged into the system
- Logged user can view registered users page
- Logged user can logout from the system

### Install and running the application:
- Clone the project from github repository: ```git svn clone https://github.com/valeriybercha/python-demos/trunk/flask-app-register-login```
- Create project virtual environment: ```python3 -m venv venv```
- Start the virtual environment: ```source venv/bin/activate```
- Install the needed libraries:
	- Flask: ```pip install flask```	
	- Flask SQLAlchemy database: ```pip install flask-sqlalchemy```
	- Flask WTForms for forms validation: ```pip install flask-wtf```
	- WTForms email validation: ```pip install wtforms[email]```
	- Flask-Login: ```pip install flask-login```
	
	OR, install all libraries from ```requirements.txt``` file: ```pip install -r requirements.txt```
- Enable the debug mode for development server: ```export FLASK_DEBUG=1```
- Start flask project: ```export FLASK_APP=app.py``` and ```flask run```
- Open the project in browser with address: ```localhost:5000```

App was created in WSL (Windows Subsystem for Linux) environment using Nano editor
