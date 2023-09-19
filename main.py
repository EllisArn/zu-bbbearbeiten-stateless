import helper
from flask import Flask, request, Response, render_template, redirect, url_for

app = Flask(__name__)


# Hier werden die Daten abgefragt und an index.html weitergegeben
@app.route("/")
def index():
    todos = helper.get_all()
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    date = request.form.get("deadline")
    category = request.form.get("category")
    description = request.form.get("description")
    helper.add(title, date=date, category=category, description=description)
    return redirect(url_for("index"))


@app.route("/create/<string:title>", methods=["GET"])
def create(title):
    helper.add(title)
    return redirect(url_for("index"))


@app.route("/update/<int:index>")
def update(index):
    helper.update(index)
    return redirect(url_for("index"))


@app.route("/download")
def get_csv():
    return Response(
        helper.get_csv(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=zu-bbbearbeiten.csv"},
    )
