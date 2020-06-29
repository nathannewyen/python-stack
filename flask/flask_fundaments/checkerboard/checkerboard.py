from flask import Flask, render_template, make_response
app = Flask(__name__)


@app.route('/')
def home():
    return "<h1> Hello, enter URL '/number' to make an checkerboard </h1>"


@app.route('/<int:x>')
def one(x):
    return render_template('index.html', rows=x, columns=x)


@app.route('/<int:x>/<int:y>')
def test(x, y):
    return render_template('index.html', rows=x, columns=y)


@app.route('/<int:x>/<color1>')
def two(x, color1):
    return render_template('index.html', rows=x, columns=x, pickcolor1=color1)


@app.route('/<int:x>/<color1>/<color2>')
def three(x, color1, color2):
    return render_template('index.html', rows=x, columns=x, pickcolor1=color1, pickcolor2=color2)


@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def four(x, y, color1, color2):
    return render_template('index.html', rows=x, columns=y, pickcolor1=color1, pickcolor2=color2)


if __name__ == "__main__":
    app.run(debug=True)
