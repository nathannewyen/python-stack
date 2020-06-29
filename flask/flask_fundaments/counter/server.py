from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def home():
    if "number" in session:
        session["number"] += 1
    else:
        session["number"] = 1
    print(session["number"])
    print(session)
    return render_template('index.html', number=session["number"])


@app.route('/addtwo', methods=["POST"])
def addtwo():
    session["number"] += 1
    return redirect('/')


@app.route('/clear', methods=["POST"])
def clear():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
