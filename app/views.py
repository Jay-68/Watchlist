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

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
  '''
  view movie page functions that returns the movie details page and its data
  '''
  return render_template('movie.html',id=movie_id)
  # add a new route with a movie function and a dynamic route <> which returns a response of a movie.html