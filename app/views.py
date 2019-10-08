from flask import render_template
from app import app

# views
@app.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
  message='Hello World Domination!'
  # passed as an argument in the render_template..
  # the message is a variable block used in the index
  return render_template('index.html',message=message)
  # import render_template from flask - takes the name of the template as its first argument