import os.path, datetime
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from sqflodo import db

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
