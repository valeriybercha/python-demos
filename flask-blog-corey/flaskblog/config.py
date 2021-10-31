# Project configuration file


class Config:
	"""
	Creating secret key string variable:
	- open python interpreter in terminal: 'python3'
	- import 'secrets' module: 'import secrets'
	- generating random token: 'secrets.token_hex(16)'
	"""
	SECRET_KEY = 'your_secret_key'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	# Mail configuration for password restoring by email
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'your_email_here'
	MAIL_PASSWORD = 'your_email_password_here'
