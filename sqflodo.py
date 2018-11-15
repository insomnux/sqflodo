import os.path, datetime
from flask import Flask, render_template, request

app = Flask(__name__)

tasklist = []

# Views
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new", methods=["POST"])
def new():
    if request.method == "POST":      
        newtask = request.form.get("task[newtask]")
        duedate = request.form.get("task[duedate]")
        tasklist.append([newtask, duedate])
        taskdict = dict(tasklist)

    return render_template("index.html", taskdict = taskdict.items())

if __name__ == "__main__":
    app.run(debug=True)
