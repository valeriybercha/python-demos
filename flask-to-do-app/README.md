# Demo task manager built with Python and Flask

### Features:
- Register a user to the database:
	- Registration form fields:		
		- Email (Unique, Length: 4 - 50)
		- Full Name (Length: 5 - 120)
		- Password (Length: 8 - 20)
		- Confirm password (EqualTo: password)
- Verification if email already exists in the database when registring a new user
- Login into the system for registered users:
	- Login form fields:
		- Email (Required)
		- Password (Required)
- Successdul message display when users are registered ir logged into the system
- Logged user can create a task
- Logged user can complete a task marking it as 'Done'
- All completed tasks will be stored in 'Completed tasks' page
- User can 'Undone' a completed task. Task will appeat in the task list again
- Logged user can update created task
- Logged user can delete created task

### Pre-requistites:
- Python should be installed: ```python3 --version```. If python is not installed: ```sudo apt install python3 python3-pip python3-venv```

### Install and run the application
- Clone the project from github repository: ```git svn clone https://github.com/valeriybercha/python-demos/trunk/flask-to-do-app```
- Create project virtual environment: ```python -m venv venv```
- Start the virtual environment server: ```source venv/bin/activate```
- Install needed libraries:
	- Flask: ```pip install flask```
	- Flask WTForms: ```pip install flask-wtf```
	- WTForms Email validation ```pip install wtforms[email]```
	- Flask SQLAlchemy: ```pip install flask-sqlalchemy```
	- Flask Login: ```pip install flask-login```
	OR, install libraries from ```requirements.txt``` file
- Enable the debug mode for development server: ```export FLASK_DEBUG=1```
- Start flask project: ```export FLASK_APP=app.py``` and ```flask run```
- Open the project in browser with address: ```localhost:5000```
