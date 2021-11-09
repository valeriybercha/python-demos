# Basic blog app created with Flask
# Programming language: Python 3.6.9
# Developer: Valeriy B.

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating 'db' database
db = SQLAlchemy(app)

# Creating default variables
default_blog_title = "Simple Flask Blog"
default_blog_description = "Demo blog created with Flask where you can add posts and pages"
default_author_name = "Author Unknown"


# Models for adding posts to the database
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	author = db.Column(db.String(30), nullable=False)
	content = db.Column(db.Text, nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	
	def __repr__(self):
		return f"Post {self.id}"
		

# Models for adding new pages to the database
class Page(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	content = db.Column(db.Text, nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	
	def __repr__(self):
		return f"Page {self.id}"


# Quering all pages
def all_pages():
	return Page.query.all()
	

# Routing for adding pages to menu 
def menu_pages():
	return render_template('base.html', pages=pages)


# Routing for adding blog description to sidebar 
def about_sidebar():
	about = default_blog_description
	return render_template('base-posts.html', about=about)


# Routing for 'Index' blog page (display all posts)
@app.route('/')
def index():
	posts = Post.query.all()
	pages = all_pages()
	default_variables = [default_blog_title, default_blog_description]
	about = default_blog_description
	return render_template('index.html', posts=posts, pages=pages, default_variables=default_variables, about=about)


# Routing for post display
@app.route('/post/<int:id>')
def posts(id):
	post = Post.query.get_or_404(id)
	pages = all_pages()
	return render_template('posts.html', post=post, pages=pages)


# Routing for adding a new post
@app.route('/add-post', methods=["POST", "GET"])
def add_post():
	if request.method == "POST":
		title = request.form['title'].title()
		if request.form['author'] == "":
			author = default_author_name
		else:
			author = request.form['author'].title()
		content = request.form['content']
		post = Post(title=title, author=author, content=content)
		db.session.add(post)
		db.session.commit()
		return redirect(url_for('index'))
	else:
		pages = all_pages()
		about = default_blog_description
		return render_template('add-posts.html', pages=pages, about=about)


# Routing for deleting posts
@app.route('/post/<int:id>/delete')
def delete_post(id):
	post_to_delete = Post.query.get_or_404(id)
	db.session.delete(post_to_delete)
	db.session.commit()
	return redirect(url_for('index'))
	

# Routing for updating posts
@app.route('/post/<int:id>/update', methods=["POST", "GET"])
def update_post(id):
	if request.method == "POST":
		updated_post = Post.query.get_or_404(id)
		updated_post.title = request.form['title'].title()
		if request.form['author'] == "":
			updated_post.author = default_author_name
		else:
			updated_post.author = request.form['author'].title()
		updated_post.content = request.form['content']
		db.session.commit()
		return redirect(url_for('index'))
	else:
		pages = all_pages()
		post = Post.query.get_or_404(id)
		return render_template('update-posts.html', post=post, pages=pages)


# Routing for 'About' page
@app.route('/about')
def about():
	pages = all_pages()
	return render_template('about.html', pages=pages)


# Routing for adding pages
@app.route('/add-page', methods=["POST", "GET"])
def add_page():
	if request.method == "POST":
		title = request.form['title'].title()
		content = request.form['content']
		post_to_add = Page(title=title, content=content)
		db.session.add(post_to_add)
		db.session.commit()
		return redirect(url_for('index'))
	else:
		pages = all_pages()
		about = default_blog_description
		return render_template('add-pages.html', pages=pages, about=about, active_add_page="active")


# Routing for 'Page' display
@app.route('/page/<int:id>')
def pages(id):
	page = Page.query.get_or_404(id)
	pages = all_pages()
	return render_template('page.html', page=page, pages=pages)


# Routing for deleting pages
@app.route('/page/<int:id>/delete')
def delete_page(id):
	page_to_delete = Page.query.get_or_404(id)
	db.session.delete(page_to_delete)
	db.session.commit()
	return redirect(url_for('index'))


# Routing for updating pages
@app.route('/page/<int:id>/update', methods=["POST", "GET"])
def update_page(id):
	if request.method == "POST":
		page_to_update = Page.query.get_or_404(id)
		page_to_update.title = request.form['title']
		page_to_update.content = request.form['content']
		db.session.commit()
		return redirect(url_for('index'))
	page = Page.query.get_or_404(id)
	pages = all_pages()
	return render_template('update-pages.html', page=page, pages=pages)


if __name__ == "__main__":
	app.run(debug=True)
