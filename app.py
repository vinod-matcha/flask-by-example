import os

# import the Flask object from the flask package
from flask import Flask

# use Flask object to create your Flask application instance with the name app. 
# You pass the special variable __name__ that holds the name of the current Python module, It’s used to tell the instance where it’s located
# Use the app instance to handle incoming web requests and send responses to the user
app = Flask(__name__)

# Use the os.environ method to import the appropriate APP_SETTINGS variables, depending on our environment
# Then set up the config in our app with the app.config.from_object method.
app.config.from_object(os.environ['APP_SETTINGS'])

# Sanity check if right variable is used in right environment
print(os.environ['APP_SETTINGS'])

# @app.route is a decorator that turns a regular Python function into a Flask view function, which converts 
# the function’s return value into an HTTP response to be displayed by an HTTP client, such as a web browser
# You pass the value '/' to @app.route() to signify that this function will respond to web requests for the URL /, which is the main URL.
@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
    
if __name__ == '__main__':
    app.run()