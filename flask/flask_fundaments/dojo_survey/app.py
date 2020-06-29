
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route('/result', methods=["GET", "POST"])
def result():
    if request.method == "POST":
        return render_template(
            "result.html",
            name=request.form["name"],
            location=request.form["location"],
            fav_language=request.form["fav-language"],
            comment=request.form["comment"]
        )
    else:
        return render_template(
            "result.html",
            name=request.args.get("name"),
            location=request.args.get("location"),
            fav_language=request.args.get("fav-language"),
            comment=request.args.get("comment")
        )


app.run(debug=True)
