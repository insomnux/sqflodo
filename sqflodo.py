import os.path, datetime
from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, Boolean, create_engine
from models import *

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

def _get_date():
    return datetime.datetime.now()

# Views
@app.route("/", methods=["GET", "POST"])
def index():
    alltasks = db.session.query(Tasks).all()
    atform = AddTaskForm(request.form)

    if request.method == "POST":
        newtask = request.form.get("newtask")

        # Format ISO date from HTML to Python date object:
        task_duedate = request.form.get("duedate")
        duedate_year = int(task_duedate[:4])
        duedate_month = int(task_duedate[5:7])
        duedate_date = int(task_duedate[8:10])
        duedate = datetime.datetime(duedate_year,duedate_month,duedate_date)

        # Check if completed
        checkcomplete = request.form.get("iscomplete")
        if checkcomplete:
            return

        row = Tasks(tdtask=newtask,lastday=duedate,complete=checkcomplete)
        db.session.add(row)
            
        db.session.commit()

    return render_template("index.html", mytasks = alltasks, atform = atform)

@app.route("/done/<int:id>")
def done(id):
    taskid = db.session.query(Tasks).filter_by(key=int(id)).first()
    taskid.complete = True
    db.session.commit()

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
