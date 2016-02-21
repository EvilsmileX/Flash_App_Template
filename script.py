# -*- coding: utf-8 -*-
# This file starts the WSGI web application.
from flask_script import Manager

# Start a development web server if executed from the command line
if __name__ == "__main__":
    
    from app import app
    manager = Manager(app)          # Setup Flask-Script

    from app.startup.db import manager as database_manager
    manager.add_command('db', database_manager)

    # Manage the command line parameters such as:
    # - python script.py runserver
    # - python script.py shell
    # - python script.py -?
    manager.run()

