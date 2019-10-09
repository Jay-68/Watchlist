# code to make requests to our api
from app import app

# getting the api key
# import the app instance and from it get the api key from the config.py file
api_key=app.config['MOVIE_API_KEY']