
from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/', methods=['GET', 'POST'])
def home():
    print(random.randint(1, 10))

    if "rightNumber" not in session:
        return redirect('/create')
    else:
        if session['resetNumber'] == True:
            return redirect('/reset')
        else:
            return render_template('index.html',
                                   rightNumber=session['rightNumber'],
                                   togglelow=session['togglelow'],
                                   togglehigh=session['togglehigh'],
                                   togglecorrect=session['togglecorrect'],
                                   toggleform=session['toggleform']
                                   )


@app.route('/create')
def create():
    session['rightNumber'] = random.randint(1, 10)
    session['resetNumber'] = False
    session['togglelow'] = "hidecontents"
    session['togglehigh'] = "hidecontents"
    session['togglecorrect'] = "hidecontents"
    session['toggleform'] = "showcontents"
    return redirect('/')


@app.route('/process', methods=["POST"])
def process():
    if int(session["rightNumber"] == int(request.form["guessNumber"])):
        session["togglelow"] = "hidecontents"
        session["togglehigh"] = "hidecontents"
        session["togglecorrect"] = "showcontents"
        session["toggleform"] = "hidecontents"
    elif int(session["rightNumber"]) < int(request.form["guessNumber"]):
        session["togglelow"] = "hidecontents"
        session["togglehigh"] = "showcontents"
        session["togglecorrect"] = "hidecontens"
        session["toggleform"] = "showcontent"
    else:
        session["togglelow"] = "showcontents"
        session["togglehigh"] = "hidecontents"
        session["togglecorrect"] = "hidecontents"
        session["toggleform"] = "showcontents"
    return redirect("/")


@app.route("/playagain", methods=["POST"])
def reset_raise():
    session["resetRandomNumber"] = True
    return redirect("/")


@app.route("/reset")
def resetSession():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
