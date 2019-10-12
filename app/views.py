from flask import render_template
from app import app
from .request import get_movies,get_movie

# views
@app.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
   # getting popular movie
  popular_movies=get_movies('popular')
  upcoming_movie=get_movies('upcoming')
  now_showing_movie=get_movies('now_playing')
  # print(popular_movies)

  title='Home - Welcome to the best Movie Review Website online'
  return render_template('index.html',title=title,popular=popular_movies,upcoming=upcoming_movie,now_showing=now_showing_movie)

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
    movie=get_movie(id)
    title=f'{movie.title}'

  return render_template('movie.html',title=title,movie=movie)
  # add a new route with a movie function and a dynamic route <> which returns a response of a movie.html