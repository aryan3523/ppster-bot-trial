from flask import Flask

# Create a Flask application
web = Flask(__name__)

# Define a route for the homepage
@web.route('/')
def hello_world():
    return 'This bot is made by AssassiN and is currently hosted and live for everyone'

# Run the application
if __name__ == '__main__':
    web.run(PORT=8080)
