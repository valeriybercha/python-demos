# Posts Flask app

from flask import Flask, render_template, request

app = Flask(__name__)


# Dummy data for posts
posts = [
	{
		'title': 'First post on the blog',
		'content': 'This is the content of the first blog post',
		'author': 'John Doe',
		'date_posted': '2021-10-01'
	},
	{
		'title': 'Second post on the blog',
		'content': 'This is the content of the second blog post',
		'author': 'John Doe',
		'date_posted': '2021-10-02'
	},
	{
		'title': 'Third post on the blog',
		'content': 'This is the content of the third blog post',
		'date_posted': '2021-10-02'
	}
]


@app.route('/')
def index():
	return render_template('posts_index.html', posts=posts)


@app.route('/posts/<int:post_id>')
def post(post_id):
	post = posts[post_id]
	return render_template('posts_post.html', post=post)	
		

if __name__ == '__main__':
	app.run(debug=True)
