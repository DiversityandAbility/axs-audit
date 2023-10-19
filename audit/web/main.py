import json
from datetime import datetime
from pathlib import Path

from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    abort,
    request,
    send_file,
)

app = Flask(__name__)


@app.route("/")
def audits_list():
    results_dir = Path("results")
    projects = [p.name for p in results_dir.iterdir() if p.is_dir()]
    return render_template("audits/list.html", page="audits", projects=projects)


@app.route("/audits/<name>/")
def audits_redirect(name):
    project_dir = Path("results") / name
    if not project_dir.is_dir():
        abort(404)
    runs = sorted([r.name for r in project_dir.iterdir() if r.is_dir()])
    return redirect(url_for("audits_get", name=name, run=runs[-1]))


@app.route("/audits/<name>/<run>/")
def audits_get(name, run):
    run_dir = Path("results") / name / run
    if not run_dir.is_dir():
        abort(404)

    runs = sorted(
        [(r.name, pretty_ts(r.name)) for r in run_dir.parent.iterdir() if r.is_dir()],
        reverse=True,
    )

    with open(run_dir / "context.json", "r") as fp:
        context = json.load(fp)

    return render_template(
        "audits/get.html",
        page="audits",
        project=name,
        run_id=run,
        run_name=pretty_ts(run),
        runs=runs,
        context=context,
    )


@app.route("/screenshot/<name>/<run>/")
def screenshot(name, run):
    # THIS IS NOT GOOD! DON'T USE PYTHON TO RETURN SCREENSHOTS!
    run_dir = Path("results") / name / run
    if not run_dir.is_dir():
        abort(404)

    url = request.args.get("url")
    id = request.args.get("id")
    with open(run_dir / "context.json", "r") as fp:
        context = json.load(fp)

    sid = context["results"][url]["screenshots"][id]
    p = run_dir / "screenshots" / f"{sid}.png"

    return send_file(p.open("rb"), mimetype="image/png")


@app.route("/docs/")
def docs():
    return render_template("docs/index.html", page="docs")


@app.route("/settings/")
def settings():
    return render_template("settings/index.html", page="settings")


@app.route("/signout/")
def signout():
    return redirect(url_for("audits_list"))


def pretty_ts(ts):
    ts = datetime.fromtimestamp(int(ts))
    return ts.isoformat()
