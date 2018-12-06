import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)

def _get_date():
    return datetime.datetime.now()

# Models
db.create_all()

class Tasks(db.Model):
    key = db.Column(db.Integer, primary_key=True)
    tdtask = db.Column(db.String(160), nullable=False)
    createdday = db.Column(db.Date, default=datetime.datetime.utcnow)
    lastday = db.Column(db.Date, default=datetime.datetime.utcnow)
    complete = db.Column(db.Boolean, default=False)


class AddTaskForm(FlaskForm):
    newtask = StringField("newtask", validators=[DataRequired()])
    duedate = DateField("duedate", format="%Y-%m-%d",
                        validators=[DataRequired()])

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
        duedate = datetime.datetime(duedate_year, duedate_month, duedate_date)

        # Check if completed
        checkcomplete = request.form.get("iscomplete")

        row = Tasks(tdtask=newtask, lastday=duedate, complete=checkcomplete)
        db.session.add(row)

        db.session.commit()
        return redirect(url_for("index"))

    return render_template("index.html", mytasks=alltasks, atform=atform)

@app.route("/done/<int:t_id>")
def done(t_id):
    taskid = db.session.query(Tasks).filter_by(key=int(t_id)).first()
    taskid.complete = True
    db.session.commit()

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
