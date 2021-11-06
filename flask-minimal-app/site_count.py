# Page counting Flask app

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
	
	"""Open the 'count.txt' file and read the stored count variable number"""
	f = open('count.txt', 'r')
	count = int(f.read())
	f.close()
	
	"""Adding plus one count every time we visit the '/' page"""
	count += 1
	
	"""Rewrite the count varible in the 'count.txt' file"""
	f = open('count.txt', 'w')
	f.write(str(count))
	f.close()
	
	return render_template('sc_index.html', count=count)
	

if __name__ == '__main__':
	app.run(debug=True)
