To run in dev:
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

To refresh db schema:

```
>>> from flaskr.db import init_db_command
>>> init_db_command()
```
