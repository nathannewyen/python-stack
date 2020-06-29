from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/play')
def bluebox():
    return render_template('index.html', times=3)


@app.route('/play/<int:x>')
def second(x):
    return render_template('index.html', times=x)


@app.route('/play/<int:r>/<color>')
def green(r, color):
    return render_template('index.html', times=r, pickcolor=color)


if __name__ == "__main__":
    app.run(debug=True)
