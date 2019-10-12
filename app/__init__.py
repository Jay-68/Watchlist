from flask import Flask
from .config import DevConfig
# initializing the bootstrap flask extension
from flask_bootstrap import Bootstrap

# initializing the application
app = Flask(__name__, instance_relative_config=True)

# the app.config.from.pyfile('config.py connects to the config.py file and all its contents are appended to the app.config)
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# to make the application use the new configurations we import the DevConfig subclass in __init__.py.
# we then use the app.config.from_object() method to set up configuration and pass the DevConfig as our arguments



# import flask class from flask module and use it to create an app instance of the class flask and pass in the variable __name__
from app import views

# initializing flask extensions
# initialized the Bootstrap class by passing in the app instance.Most extensions are initialized this way.
bootstrap = Bootstrap(app)