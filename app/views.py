from flask import render_template
from app import app

# views
@app.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
  return render_template('index.html')
  # import render_template from flask - takes the name of the template as its first argument