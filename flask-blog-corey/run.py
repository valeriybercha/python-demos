# Flask Application created under Corey Schaffer youtube tutorials

from flaskblog import create_app

app = create_app()

""" 
	Activating the debug mode.
	Run in terminal:
	- 'export FLASK_DEBUG=1'
	- 'flask run' or 'python flaskblog.py'
"""
if __name__=='__main__':
	app.run(debug=True)

