from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def redirect():
    session['strawberry'] = request.form['strawberry']
    session['raspberry'] = request.form['raspberry']
    session['apple'] = request.form['apple']
    session['blackberry'] = request.form['blackberry']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    return redirect('/checkout')


@app.route('/checkout', methods=['POST'])
def checkout():
    # Count fruits customer made
    count = int(int(request.form["strawberry"]) + int(request.form["raspberry"]) +
                int(request.form["apple"]) + int(request.form["blackberry"]))
    print("Charging " + request.form["first_name"] + " " +
          request.form["last_name"] + " for " + str(count) + " fruits")
    # End of Count
    return render_template('checkout.html',
                           strawberry=session['strawberry'],
                           raspberry=session['raspberry'],
                           apple=session['apple'],
                           blackberry=session['blackberry'],
                           first_name=session['first_name'],
                           last_name=session['last_name'],
                           student_id=session['student_id'],
                           count=count
                           )


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    date = dateutil.parser.parse(date)
    native = date.replace(tzinfo=None)
    format = '%b %d, %Y'
    return native.strftime(format)


if __name__ == "__main__":
    app.run(debug=True)
    # session['strawberry'] = request.form['strawberry']
    # session['raspberry'] = request.form['raspberry']
    # session['apple'] = request.form['apple']
    # session['blackberry'] = request.form['blackberry']
    # session['first_name'] = request.form['first_name']
    # session['last_name'] = request.form['last_name']
    # session['student_id'] = request.form['student_id']
    # session[count] = int(count)
