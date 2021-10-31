# Demo blog with Flask framework on Python

This blog is created under [Corey Schafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) youtube tutorials

### Blog functionality:

- User registration
- User login
- Add post
- Update post
- Delete post
- Blog pagination
- Display posts by author

## Setting up and create a blog using Flask

Pre-requisites:
- Python should be already installed on the system. To check this: ```python3 --version```
- Python virtual environment package should be installed: ```sudo apt install python3-venv```

Additional for Linux: update and install header files and static libraries for Python Dev:
```
sudo apt-get install python-dev   # for python2.x installs
sudo apt-get install python3-dev  # for python3.x installs
```

#### Modules and packages needed to be installed:

- Flask: ```pip install flask```
- Flask forms: ```pip install flask-wtf```
- Wtf forms 'email_validator' package: ```pip install wtforms[email]```
- Data base 'SQLAlchemy' for Flask: ```pip install flask-sqlalchemy```
- 'Flask-Bcrypt' for hashing passwords: ```pip install flask-bcrypt```
- Flask Login: ```pip install flask-login```
- 'Pillow' package for resizing images: ```pip install Pillow```
- 'Flask Email' for sending emails: ```pip install flask-mail```

### Setting up a Flask project on Linux:

1. Create a project folder: ```mkdir flask-blog```
2. Navigate to the project folder: ```cd flask-blog```
3. Create a virtual environment inside your project directory: ```python3 -m venv venv```
4. Activate the virtual environment: ```source venv/bin/activate```
5. Install Flask: ```pip install Flask```
6. To verify if Flask was installed on the system: ```python -m flask --version```
7. Create the simpliest 'Hello, World!' program. Create a python file: ```touch flaskblog.py```
8. Open the 'flaskblog.py' file and paste in it the following code:
```
from flask import Flask
app = Flask(__name__)

@ app.route('/')
def hello_world():
    return "Hello, World!"
```
9. Launch the development server: ```export FLASK_APP=flaskblog.py``` and then run the Flask app: ```flask run```
10. The ```http://127.0.01:5000``` or ```http://localhost:5000``` server address should be displayed. Open it in the browser and the 'Hello, World!' message should be displayed
11. Use ```deactivate``` command to stop the server

### Start the development server in Debug mode

1. Paste the following code in the python file ```flaskblog.py```:
```
if __name__=='__main__':
	app.run(debug=True)
```
2. Run the command: ```export FLASK_DEBUG=1```
3. Then run the flask app with the command: ```flask run``` or ```python flaskblog.py```

### Flask Blog Project Structure (before creating packages)

- flask-blog (project directory):
	- venv (virtaul environment folder: ```python3 -m venv venv```)
	- templates (templates folder: home.html, layout.html ...):
		- layout.html
		- home.html
		- about.html
		- login.html
		- register.html
	- static (static folder: css, js files ...):
		- main.css
	- flaskblog.py (main project file)
	- forms.py (Login and Registration logic creation)
	- site.db (blog SQLite database)
	- models.py (storing project models)

### Creating and testing SQLite project database with SQLAlchemy

1. Install Flask SQLAlchemy package: ```pip install flask-sqlalchemy```
2. Create the tables for the project:
```
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	post = db.relationship('Post', backref='author', lazy=True)
	
	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
		user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	def __repr__(self):
		return f"User('{self.title}', '{self.date_posted}')"
```
3. Open ```python3``` in terminal in the virtual environment
4. From application 'flaskblog' import 'db', 'User' and 'Post':
	- ```from flaskblog import db```
	- ```from flaskblog import User, Post```
5. Create a database with the command: ```db.create_all()``` "site.db" file shoulf be created in the project directory
6. Create a new user:
```
user_1 = User(username="John", email="JohnDoe@company.com", password="password")
db.session.add(user_1)
db.session.commit()
```
7. Verify if users were added to database (will display all the users): ```User.query.all()```
8. Verify the first user added: ```User.query.first()```
9. Filter users added by name (case sensitive): ```User.query.filter_by(username="John").all()```
10. Additional queries:
	- Set up a variable "user" ```user = User.query.first()```
	- display user id: ```user.id```
	- display the user by id: ```User.query.get(1)```
	- display users posts: ```user.post```
11. Create a new post:
```
post_1 = Post(title="First blog post", content="First post content", user_id=user.id)
db.session.add(post_1)
db.session.commit()
```
12. Additional queries:
	- ```user = User.query.get(1)```	
	- ```for post in user.post: print(post)```
	- ```post.author```
13. Delete all data: ```db.drop_all()```
14. Create a new blank database: ```db.create_all()```

### Creating project packages - Package Structure

- flask-blog (project directory):
	- venv (virtaul environment folder: ```python3 -m venv venv```)
	- run.py (renaming 'flaskblog.py' in the 'run.py' file)
	- flaskblog (project python package):
		- __init__.py (project package file)	
		- templates (templates folder: home.html, layout.html ...):
			- layout.html
			- home.html
			- about.html
			- login.html
			- register.html
		- static (static folder: css, js files ...):
			- main.css
		- forms.py (Login and Registration logic creation)
		- site.db (blog SQLite database)
		- models.py (storing project models)
		- routes.py (project routes file)

Note: After creating project packages when deleting or creating tables in database an error could occur. The solution is to create and push application context when deleting or creating tables in project database. If it is needed to remove or create tables in the database:
- ```from flaskblog import db```
- ```from flaskblog import create_app```
- ```app = create_app()```
- ```app.app_context().push()```
- ```db.create_all()``` or ```db.drop_all()```

### Using Flask-Bcrypt package for hashing passwords in the application project

Pre-requisites (for Linux):
- In order to install 'py-bcrypt' package Python Development Headers need to be installed: ```sudo apt-get install python3-dev```

Steps:
1. Install the package: ```pip install flask-bcrypt```
2. Open ```python``` in terminal
3. Import the package: ```from flask_bcrypt import Bcrypt```
4. Initiate a variable ```bcrypt```: ```bcrypt = Bcrypt()```
5. Generate a hashed version of 'testing' password: ```bcrypt.generate_password_hash('testing').decode('utf-8')```
6. Create a variable 'hashed_pas': ```hashed_pas = bcrypt.generate_password_hash('testing').decode('utf-8')```
7. Verify if the hashed variable == hashed password: ```bcrypt.check_password_hash(hashed_pas, 'testing')```
8. The result should equal ```True```
