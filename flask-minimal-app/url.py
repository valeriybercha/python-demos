from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return "<h1>Home Page</h1><ul><p>Other pages</p><li>/about</li><li>/login</li><li>/user/john</li></ul>"
	

@app.route("/about")
def about():
	return "<h1>About Page</h1>"
	

@app.route("/login")
def login():
	return "<h1>Login Page</h1>"


@app.route("/user/<username>")
def user(username):
	return f"<h1>{username.title()} Page</h1>"

	
with app.test_request_context():	
	print(url_for('home'))
	print(url_for('about'))
	print(url_for('login'))
	print(url_for('user', username="john"))


if __name__ == '__main__':
	app.run(debug=True)
