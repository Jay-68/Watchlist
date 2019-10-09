from flask import Flask
from .config import DevConfig

# initializing the application
# the instance_relative_config allows us to connect to the instance/ folder when the app instance is created
app=Flask(__name__,instance_relative_config=True)

# setting up configuration
# the app.config.from.pyfile('config.py connects to the config.py file and all its contents are appended to the app.config)
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# to make the application use the new configurations we import the DevConfig subclass in __init__.py.
# we then use the app.config.from_object() method to set up configuration and pass the DevConfig as our arguments

from app import views

# import flask class from flask module and use it to create an app instance of the class flask and pass in the variable __name__