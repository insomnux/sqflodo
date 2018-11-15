import os.path, datetime
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

tasklist = []

# Models
Base = declarative_base()

def _get_date():
    return datetime.datetime.now()

class Tasks(Base):
    __tablename__ = "tasks"
    key = Column(Integer, primary_key=True)
    tdtask = Column(String(160), nullable=False)
    createdday = Column(Date, default=_get_date)
    lastday = Column(Date, default=_get_date)
    complete = Column(Boolean, default=False)

# Create database engine
db_path = os.path.join(os.path.dirname(__file__), "tasks.db")
db_uri = "sqlite:///{}".format(db_path)
engine = create_engine(db_uri)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Views
@app.route("/", methods=["GET", "POST"])
def index():
    alltasks = session.query(Tasks).all()
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
        session.add(row)
            
        session.commit()
            
    return render_template("index.html", mytasks = alltasks)


    '''
    if request.method == "POST":      
        newtask = request.form.get("task[newtask]")
        duedate = request.form.get("task[duedate]")
        tasklist.append([newtask, duedate])
        taskdict = dict(tasklist)
    else:
        tasklist.clear()
        taskdict = {}

    return render_template("index.html", taskdict = taskdict.items())
    '''


if __name__ == "__main__":
    app.run(debug=True)
