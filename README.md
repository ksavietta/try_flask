To run in dev:
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

To install xmltodict:
```
pip install xmltodict
```

To refresh db schema:

```
>>> from flaskr.db import init_db_command
>>> init_db_command()
```

front end vue.js setup (optional at this point):
# install dependencies
`npm install`

# serve with hot reload at localhost:8080
`npm run dev`

# build for production with minification
`npm run build`

# build for production and view the bundle analyzer report
`npm run build --report`
