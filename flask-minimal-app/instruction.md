# Minimal Flask Apps

### Pre-requisites:
- Python must be installed on the system: ```python3 --version``` to verify python installation
- Python virtual environment package should be installed: ```sudo apt install python3-venv```

Steps:
1. Create a project directory: ```mkdir flask-minimal-app```
2. Navigate to the project folder: ```cd flask-blog```
3. Create a virtual environment inside your project directory: ```python3 -m venv venv```
4. Activate the virtual environment: ```source venv/bin/activate```
5. Install Flask: ```pip install Flask```
6. To verify if Flask was installed on the system: ```python -m flask --version```
7. Create the simpliest 'Hello, World!' program. Create a python file: ```touch hello.py```
8. Open the 'hello.py' file and paste in it the following code:
```
from flask import Flask
app = Flask(__name__)

@ app.route('/')
def hello_world():
    return "<h1>Hello, World!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
```
9. Launch the development server: ```export FLASK_APP=flaskblog.py``` and then run the Flask app: ```flask run```
10. The ```http://127.0.01:5000``` or ```http://localhost:5000``` server address should be displayed. Open it in the browser and the 'Hello, World!' message should be displayed
11. Use ```deactivate``` command to stop the server


### Creating databses

- Create a python file: ```touch databases.py```
- Paste the minimal flask code in it:
```
from flask import Flask, render_template

app = Flask(__name__)

@ app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
```
- Install in the project virtual environment ```source venv/bin/activate``` the 'SQL Alchemy' database: ```pip install flask-sqlalchemy```
- Import 'SQL Alchemy' library: ```from flask_sqlalchemy import SQLAlchemy
- Create an app configuration for the database: ```app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
- Create the database: ```db = SQLAlchemy(app)
- Create 'Post' model for the database:
```
class BlogPost(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	content = db.Column(db.Text, nullable=False)
	author = db.Column(db.String(50), nullable=False, default='Author Unknown')
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	
	def __repr__(self):
		return 'Blog post ' + str(self.id)
```
- Open 'python' in terminal ```python```
- Import the database: ```from app databases import db```
- Create the database: ```db.create_all()```
- Testing the created database:
	- ```from databases import BlogPost``` (import the 'BlogPost model created earlier')
	- ```posts = BlogPost``` (creating a 'posts' variable)
	- ```posts.query.all()``` (displaying all the posts from the database. An empty list should be displayed)
	- Adding records to the database:
		- ```post1 = BlogPost(title='First Blog Post', content='First blog post content', author='Sammy Lee')``` (creating 'post1' variable with data to be added to the database)
		- ```db.session.add(post1)``` (adding data to the database)
		- ```db.session.commit()``` (commit all the changes to the database)
	- Testing the database:
		- ```posts.query.all()``` (displaying all posts)
		- ```posts.query.all()[0].title``` (display the title of the first post)
		- ```posts.query.get(1)``` (display the second post created by id)
- Additionally we can create a template to display the posts:
	- ```from flask import render_template``` (importing render template module)
	- ```touch templates/databases_index.html``` (creating a new html file in the templates directory)
	- copy the data from the 'posts_index.html' to the new created file
	- modify the index function in the 'databases.py' file:
	```
	@app.route('/')
	def index():
		posts = BlogPost.query.all()
		return render_template('databases_index.html', posts = posts)
	```
