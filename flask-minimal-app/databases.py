# Minimalistic app on Flask with SQLAlchemy database

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# App configuration file for the database creation
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating the 'db' database
db = SQLAlchemy(app)


# Creating 'Post' models for the database
class BlogPost(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	content = db.Column(db.Text, nullable=False)
	author = db.Column(db.String(50), nullable=False, default='Author Unknown')
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	
	def __repr__(self):
		return 'Blog post ' + str(self.id)


@app.route('/')
def index():
	posts = BlogPost.query.all()
	return render_template('databases_index.html', posts=posts)
	

if __name__ == '__main__':
	app.run(debug=True)
