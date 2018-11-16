import os.path, datetime
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, Boolean, create_engine

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), "tasks.db")
db_uri = "sqlite:///{}".format(db_path)
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
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

# Views
@app.route("/", methods=["GET", "POST"])
def index():
    alltasks = db.session.query(Tasks).all()
    if request.method == "POST":
        newtask = request.form.get("task[newtask]")

        # Format ISO date from HTML to Python date object:
        task_duedate = request.form.get("task[duedate]")
        duedate_year = int(task_duedate[:4])
        duedate_month = int(task_duedate[5:7])
        duedate_date = int(task_duedate[8:10])
        duedate = datetime.datetime(duedate_year,duedate_month,duedate_date)
        #duedate = Tasks(lastday=duedatedateobj)

        row = Tasks(tdtask=newtask,lastday=duedate,complete=False)
        db.session.add(row)
            
        db.session.commit()
            
    return render_template("index.html", mytasks = alltasks)


if __name__ == "__main__":
    app.run(debug=True)
