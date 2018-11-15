import os.path, datetime
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

tasklist = []

# Views
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":      
        newtask = request.form.get("task[newtask]")
        duedate = request.form.get("task[duedate]")
        tasklist.append([newtask, duedate])
        taskdict = dict(tasklist)
    else:
        tasklist.clear()
        taskdict = {}

    return render_template("index.html", taskdict = taskdict.items())


if __name__ == "__main__":
    app.run(debug=True)
