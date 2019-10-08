from flask import Flask
from .config import DevConfig

# initializing the application
app=Flask(__name__)

# setting up configuration
app.config.from_object(DevConfig)

# to make the application use the new configurations we import the DevConfig subclass in __init__.py.
# we then use the app.config.from_object() method to set up configuration and pass the DevConfig as our arguments

from app import views

# import flask class from flask module and use it to create an app instance of the class flask and pass in the variable __name__