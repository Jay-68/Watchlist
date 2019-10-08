from flask import Flask

# initializing the application
app=Flask(__name__)
from app import views

# import flask class from flask module and use it to create an app instance of the class flask and pass in the variable __name__