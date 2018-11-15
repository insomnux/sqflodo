sqflodo
=======

Todo list with [Flask](http://flask.pocoo.org/) and [SQLite](https://www.sqlite.org/)

## Usage:

1. Clone the repo, create virtual env - see [Virtualenv](https://virtualenv.pypa.io/en/latest/) and install requirements:

```sh
# sh
git clone https://github.com/insomnux/sqflodo.git
cd sqflodo
virtualenv flask
source flask/bin/activate
# to quit virtual env:
# deactivate
pip install -r requirements.txt
```

2. Create `tasks.db` database:

```sh
# sh
touch tasks.db
python
```

```python
# python
from sqflodo import tasksdb
db.create_all()
quit()
```

3. Start the application:

```sh
python sqflodo
```

and browse to [localhost:5000](http://localhost:5000)
