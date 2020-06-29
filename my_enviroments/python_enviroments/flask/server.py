# Import Flask to allow us to create our app
from flask import Flask
# Create a new instance of the Flask class called "app"
app = Flask(__name__)
# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.errorhandler(404)
def error404(error):
    return "Sorry no respone. Try again"


@app.route('/dojo')
def dojo():
    return "Hello Dojo!"


@app.route('/say/flask')
def say():
    return "Hi Flask"


@app.route('/say/michael')
def michael():
    return "Hi Michael"


@app.route('/say/john')
def john():
    return "Hi John"


@app.route('/repeat/<int:id>/<word>')
def repeat(id, word):
    output = ""
    for i in range(0, id, 1):
        output += word
    return output

# app.run(debug=True) should be the very last statemen


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
