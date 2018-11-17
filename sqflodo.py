import os.path, datetime
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, Boolean, create_engine
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), "tasks.db")
db_uri = "sqlite:///{}".format(db_path)
app.config.update(dict(
        SQLALCHEMY_DATABASE_URI = db_uri,
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        SECRET_KEY = "secretkey",
        WTF_CSRF_SECRET_KEY= "supersecretkey"
        ))
db = SQLAlchemy(app)


# Models

def _get_date():
    return datetime.datetime.now()

class Tasks(db.Model):
    key = db.Column(db.Integer, primary_key=True)
    tdtask = db.Column(db.String(160), nullable=False)
    createdday = db.Column(db.Date, default=datetime.datetime.utcnow)
    lastday = db.Column(db.Date, default=datetime.datetime.utcnow)
    complete = db.Column(db.Boolean, default=False)

class AddTaskForm(FlaskForm):
    newtask = StringField("newtask", validators=[DataRequired()])
    duedate = DateField("duedate", format="%Y-%m-%d", validators=[DataRequired()])


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


if __name__ == "__main__":
    app.run(debug=True)
