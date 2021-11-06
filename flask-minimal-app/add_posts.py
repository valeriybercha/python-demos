# Add posts app on Flask

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from databases import BlogPost, db

app = Flask(__name__)

# App configuration file for the database creation
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Display all posts configuration
@app.route('/')
def all_posts():
	posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()
	return render_template('add-posts-all.html', posts=posts)


# Add a new post configuration
@app.route('/add-post', methods=['GET', 'POST'])
def add_posts():
	if request.method == "POST":
		post_title = request.form['title'].title()
		if request.form['author'] == "":
			post_author = "Author Unknown"
		else:
			post_author = request.form['author'].title()
		post_content = request.form['content']
		new_post = BlogPost(title=post_title, author=post_author, content=post_content)
		db.session.add(new_post)
		db.session.commit()
		return redirect(url_for('all_posts'))
	return render_template('add-posts.html')


# Detailed post view configuration
@app.route('/posts/<int:post_id>')
def post(post_id):
	post = BlogPost.query.get_or_404(post_id)
	return render_template('add-posts-posts.html', post=post)
	

# Delete a post configuration
@app.route('/posts/delete/<int:post_id>')
def delete_post(post_id):
	post = BlogPost.query.get_or_404(post_id)
	db.session.delete(post)
	db.session.commit()
	return redirect(url_for('all_posts'))
	

# Update a post configuration
@app.route('/posts/update/<int:post_id>', methods=["POST", "GET"])
def update_post(post_id):
	if request.method == "POST":
		updated_post = BlogPost.query.get_or_404(post_id)
		updated_post.title = request.form['title'].title()
		updated_post.author = request.form['author'].title()
		updated_post.content = request.form['content']
		db.session.commit()
		return redirect(url_for('all_posts'))
	else:
		post = BlogPost.query.get_or_404(post_id)
		return render_template('add-posts-update.html', post=post)


db.init_app(app)

if __name__ == '__main__':
	app.run(debug=True)
