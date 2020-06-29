from flask import Flask, render_template, make_response
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/users')
def members():
    users = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
    return render_template('users.html', data=users)


if __name__ == "__main__":
    app.run(debug=True)
