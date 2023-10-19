from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("audits/list.html", page="audits")


@app.route("/docs/")
def docs():
    return render_template("docs/index.html", page="docs")


@app.route("/settings/")
def settings():
    return render_template("settings/index.html", page="settings")


@app.route("/signout/")
def signout():
    return redirect(url_for("home"))
