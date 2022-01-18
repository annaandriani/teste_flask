from flask import Flask, request, session, redirect, url_for
from flask import render_template

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def add(form):
    if not "rows" in session:
        session["rows"] = []

    title = form["title"]
    message = form["message"]
    userid = form["userid"]
    session["rows"].append({"title": title, "userid": userid, "message": message, "status": False})


    session.modified = True
    return f'title: {title},userid:{userid}, message: {message}'

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        return add(request.form)
    if "rows" in session:
        return render_template("index.html", rows = session["rows"])
    return render_template("index.html")

@app.route("/clean")
def clean():
    if "rows" in session:
        session.pop("rows", None)

    return redirect(url_for('home'))
