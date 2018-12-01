import os

db_path = os.path.join(os.path.dirname(__file__), "tasks.db")
db_uri = "sqlite:///{}".format(db_path)

db_path = os.path.join(os.path.dirname(__file__), "tasks.db")
db_uri = "sqlite:///{}".format(db_path)

SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "secretkey"
WTF_CSRF_SECRET_KEY= "supersecretkey"
