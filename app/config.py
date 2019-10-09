class config:
  '''
  general configuration parent class
  '''
  MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'

class prodConfig(config):
  '''
  Production configuration child class
  
  Args:
    Config:The parent configuration class with General configuration settings
  '''
  pass

class DevConfig(config):
  '''
  Development configuration child class

  Args:
    Config:The parent configuration class with general configuration settings
  '''
  DEBUG=True

# created three classes. the parent Config class with configurations for both development stages and and production stages.
# prodConfig subclass inherits from the Config class parent and contains configurations that are used in the production stages
# the DevConfig subclass contains configurations that are used in the development stages of the application
# DEBUG=True allows for debugging mode in the application