# Flask App Template

The code (template) is designed for a simple Flask app with several useful Flask modules. It's used to generate a web APIs or pages quickly for development, and been deployed by uWSGI in production environment. It's also a good practice for you to write your next Flask app.

## Cloning the code base

We assume that you have `git` installed.

	# Clone the repository
	cd /path/to/app
	https://github.com/viney-shih/Flask_App_Template.git
	
## Install Dependencies

	pip install -r requirements.txt

## Configuring the app

Before using this app, we need to configure the unique `SECRET KEY` and `DATABASE URL`.

Initialize your setting from example

	cd path/to/app
	cp config/env_settings.py.example config/env_settings.py
	
Edit `SECRET_KEY` in different apps

	# Fill in the SECRET_KEY via the following command
	import os; os.urandom(24)

Edit `SQLALCHEMY_DATABASE_URI` 

	# For MySQL user, you could fill in with the following format
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost/<DB_NAME>'

## Initializing the Database

	# Create DB tables
	python script.py db create
	
	# For more details
	python script.py db -?
	
## Running the app

	# Start Flask server
	python script.py runserver [-h host] [-p port] [--debug] [--reload]
	
	# For more details
	python script.py -?

## References

* [Flask](http://flask.pocoo.org/)
* [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/)
* [Flask-WTF](https://flask-wtf.readthedocs.org)
* [Flask-Flask-Script](https://flask-script.readthedocs.org)
* [Flask-User starter app](https://github.com/lingthio/Flask-User-starter-app)

