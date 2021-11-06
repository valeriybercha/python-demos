# Flask Minimal App - Hello World page

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
	return f"<h1>Hello, World!</h1>"
	
if __name__ == '__main__':
    app.run(debug=True)
