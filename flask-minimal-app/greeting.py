# Simplistic greeting Flask app

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "<h1>Hello there! Type your name in the browser address bar (right after '/', e.g.: '/john')</h1>"

@app.route("/<user>")
def greetings(user):
	return f"<h1>Hello, {user.title()}! Great to see you here</h1>"
	
if __name__ == '__main__':
	app.run(debug=True)
